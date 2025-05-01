import shutil
import json
import unittest
import os

from src import Parser, FULL_SGX


FIX_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), "fixtures"))


def create_fst_config(json_path: str, dictionary: dict) -> dict:
    with open(json_path) as f:
        config = json.load(f)
    config["test"] = True
    if dictionary:
        config["dictionary"] = dictionary
    config["name"] = "testy"
    return config


def import_fst_files(config) -> list:
    # identify required files
    files = [f for f in config["rules_files"]]
    if type(config["dictionary"]) is str:
        if not config["dictionary"][:4] == "test":
            files.append(config["dictionary"])
    # copy those files to fixtures directory
    new_files = []
    for file in files:
        orig = os.path.join(os.path.dirname(__file__), "../fst", file)
        dest = os.path.join(os.path.dirname(__file__), "fixtures", file)
        shutil.copy(orig, dest)
        new_files.append(dest)
    # copy lexc files to directory in fixtures
    orig_lexc = orig = os.path.join(os.path.dirname(__file__), "../fst/lexc")
    dest_lexc = orig = os.path.join(os.path.dirname(__file__), "fixtures/lexc")
    shutil.copytree(orig_lexc, dest_lexc)

    return new_files


def cleanup_fst_files(fixture_files) -> None:
    # remove rules files
    for file in fixture_files:
        os.remove(file)
    # remove lexc directory
    lexc = os.path.join(os.path.dirname(__file__), "fixtures/lexc")
    shutil.rmtree(lexc)
    # remove foma directory
    foma = os.path.join(os.path.dirname(__file__), "fixtures/foma")
    shutil.rmtree(foma)


class TestFSTOutput(unittest.TestCase):

    @classmethod
    def setUpClass(cls, json_config, dictionary) -> None:
        cls.config = create_fst_config(json_config, dictionary)
        cls.added_files = import_fst_files(cls.config)
        cls.fst = Parser(cls.config)

    @classmethod
    def tearDownClass(cls) -> None:
        cleanup_fst_files(cls.added_files)

    def checkManyInFST(
        self,
        stem_gloss: str,
        expected_map: list[tuple[str, list[str]]],
    ):
        """
        Check the output of a stem and any number of conjugations
        against the FST.

        Arguments:
        - stem: string
            Example: "w$aalp+N"
        - expected_map: a dictionary or list of tuples consisting of
            - suffixes to be concatenated with the stem (strings)
            - list of expected output forms for that concatenation
            Example:
                {"": ["waalp"], "-ATTR": ["waalba", "waalbm"]} as dict
                [("", ["waalp"]), ("-ATTR", ["waalba", "waalbm"])] as tuple
        """
        if type(expected_map) is dict:
            expected_map = expected_map.items()

        for suffix, expected_forms in expected_map:
            gloss = stem_gloss + suffix
            result_list = self.fst.generate(gloss)
            with self.subTest(gloss=gloss):
                for expected in expected_forms:
                    self.assertIn(expected, result_list)
                self.assertEqual(
                    len(result_list),
                    len(expected_forms),
                    f"{gloss} should have {len(expected_forms)} results",
                )
