import unittest
import unicodedata as uc

from src import helpers

"""
Tests helper functions having to do with case changing,
stress annotation, and (TODO) git orthography.
"""


def test_normalize(self):
    input_str = "ẅa̱ḵg̲x_üü"
    provided_list = [uc.normalize("NFC", input_str), uc.normalize("NFD", input_str)]
    expected_lexc = uc.normalize("NFC", "ẅa_k_g_x_üü")
    expected_macr = uc.normalize("NFC", "ẅa̱ḵg̱x̱üü")

    for provided in provided_list:
        with self.subTest(provided=provided):
            self.assertEqual(helpers.convert_to_underscore(provided), expected_lexc)
            self.assertEqual(helpers.convert_to_macron(provided), expected_macr)


class TestCamelcase(unittest.TestCase):
    def test_singleword(self):
        result = helpers.camelcase("hello")
        self.assertEqual(result, "Hello")

    def test_multiword(self):
        result = helpers.camelcase("hello world")
        self.assertEqual(result, "HelloWorld")


class TestStressMarking(unittest.TestCase):

    def test_stress_unknown(self):
        inputwds = ["bat"]
        result = helpers.assign_stress(inputwds, "?")

        self.assertEqual(["bat"], result)

    def test_stress_blank_CV(self):
        inputwds = ["ba"]
        result = helpers.assign_stress(inputwds, "")

        self.assertEqual(["b$a"], result)

    def test_stress_blank_CVC(self):
        inputwds = ["bat"]
        result = helpers.assign_stress(inputwds, "")

        self.assertEqual(["b$at"], result)

    def test_stress_blank_CVVC(self):
        inputwds = ["baat"]
        result = helpers.assign_stress(inputwds, "")

        self.assertEqual(["b$aat"], result)

    def test_stress_one_CV(self):
        inputwds = ["ba"]
        result = helpers.assign_stress(inputwds, "1")

        self.assertEqual(["b$a"], result)

    def test_stress_one_CVC(self):
        inputwds = ["bat"]
        result = helpers.assign_stress(inputwds, "1")

        self.assertEqual(["b$at"], result)

    def test_stress_one_CVVC(self):
        inputwds = ["baat"]
        result = helpers.assign_stress(inputwds, "1")

        self.assertEqual(["b$aat"], result)

    def test_stress_one_CVCV(self):
        inputwds = ["baba"]
        result = helpers.assign_stress(inputwds, "1")

        self.assertEqual(["b$aba"], result)

    def test_stress_one_CVVCV(self):
        inputwds = ["baaba"]
        result = helpers.assign_stress(inputwds, "1")

        self.assertEqual(["b$aaba"], result)

    def test_stress_two_CVCV(self):
        inputwds = ["baba"]
        result = helpers.assign_stress(inputwds, "2")

        self.assertEqual(["bab$a"], result)

    def test_stress_two_CVVCV(self):
        inputwds = ["baaba"]
        result = helpers.assign_stress(inputwds, "2")

        self.assertEqual(["baab$a"], result)

    def test_stress_two_echoCVVV(self):
        inputwds = ["baa'a"]
        result = helpers.assign_stress(inputwds, "2")

        self.assertEqual(["baa'$a"], result)

    def test_stress_multiword_two(self):
        inputwds = ["baba", "bibatxws"]
        result = helpers.assign_stress(inputwds, "2")

        self.assertEqual(["bab$a", "bib$atxws"], result)

    def test_stress_multiword_two_four(self):
        inputwds = ["baba", "bibaxbaba"]
        result = helpers.assign_stress(inputwds, "2; 4")

        self.assertEqual(["bab$a", "bibaxbab$a"], result)

    def test_stress_multistress_onefour(self):
        inputwds = ["biibaxbaba"]
        result = helpers.assign_stress(inputwds, "1,4")

        self.assertEqual(["b$iibaxbab$a"], result)

    def test_stress_stress_outofrange(self):
        with self.assertRaises(IndexError):
            inputwds = ["baat"]
            helpers.assign_stress(inputwds, "4")

    def test_stress_no_onset_single(self):
        inputwds = ["aa"]
        result = helpers.assign_stress(inputwds, "1")

        self.assertEqual(["$aa"], result)

    def test_stress_no_onset_initial(self):
        inputwds = ["aba"]
        result = helpers.assign_stress(inputwds, "1")

        self.assertEqual(["$aba"], result)

    def test_stress_no_onset_later(self):
        inputwds = ["aba"]
        result = helpers.assign_stress(inputwds, "2")

        self.assertEqual(["ab$a"], result)

    def test_stress_diaresis_only(self):
        inputwds = ["düü"]
        result = helpers.assign_stress(inputwds, "1")

        self.assertEqual(["d$üü"], result)

    def test_stress_diaresis_two(self):
        inputwds = ["gügü"]
        result = helpers.assign_stress(inputwds, "2")

        self.assertEqual(["güg$ü"], result)


if __name__ == "__main__":
    unittest.main()
