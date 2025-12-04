import unittest
from test import TestFSTOutput, FULL_SGX

"""
This suite puts some test words through the Sgx parser and checks
that inflectional morphology is added correctly.

These tests use the actual FST rules but do NOT use the dict.csv file.
Instead, you provide individual test words.
"""


class TestPlainStops(TestFSTOutput):

    @classmethod
    def setUpClass(cls):
        test_stems = {
            "Noun": [
                "ch$ayp",
                "g_$oot",
                "nts'$i'its",
                "b$a_x_bog_mgyemk",
                "w$a_t'ukw",
                "han$a_'a_x_",
            ]
        }
        super().setUpClass(FULL_SGX, test_stems)

    def test_plainP(self):
        stem = "ch$ayp+N"
        expected_map = [
            ("", ["chayp"]),
            ("-1SG.II", ["chaybi", "chaybu"]),
            ("-1PL.II", ["chaybm"]),
            ("-2SG.II", ["chaybn"]),
            ("-2PL.II", ["chaypsm"]),
            ("-3.II", ["chaypt"]),
            ("[-3.II]=CN.IRR", ["chaypł"]),
            ("[-3.II]=CN", ["chaybi"]),
            ("[-3.II]=PN", ["chayps"]),
            ("-SX", ["chaybit"]),
            ("-ATTR", ["chaybm", "chayba"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_plainT(self):
        stem = "g_$oot+N"
        expected_map = [
            ("", ["g̱oot"]),
            ("-1SG.II", ["g̱oodi", "g̱oodu"]),
            ("-1PL.II", ["g̱oodm"]),
            ("-2SG.II", ["g̱oodn"]),
            ("-2PL.II", ["g̱ootsm"]),
            ("-3.II", ["g̱oot"]),
            ("[-3.II]=CN.IRR", ["g̱ootł"]),
            ("[-3.II]=CN", ["g̱oodi"]),
            ("[-3.II]=PN", ["g̱oots"]),
            ("-SX", ["g̱oodit"]),
            ("-ATTR", ["g̱oodm", "g̱ooda"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_plainTS(self):
        stem = "nts'$i'its+N"
        expected_map = [
            ("", ["nts'i'its"]),
            ("-1SG.II", ["nts'i'itsi", "nts'i'itsu"]),
            ("-1PL.II", ["nts'i'itsm"]),
            ("-2SG.II", ["nts'i'itsn"]),
            ("-2PL.II", ["nts'i'itsism"]),
            ("-3.II", ["nts'i'itst"]),
            ("[-3.II]=CN.IRR", ["nts'i'itsł"]),
            ("[-3.II]=CN", ["nts'i'itsi"]),
            ("[-3.II]=PN", ["nts'i'its"]),
            ("-SX", ["nts'i'itsit"]),
            ("-ATTR", ["nts'i'itsm", "nts'i'itsa"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_plainK(self):
        stem = "b$a_x_bog_mgyemk+N"
        expected_map = [
            ("", ["ba̱x̱bog̱mgyemk"]),
            ("-1SG.II", ["ba̱x̱bog̱mgyemgi", "ba̱x̱bog̱mgyemgu"]),
            ("-1PL.II", ["ba̱x̱bog̱mgyemgm"]),
            ("-2SG.II", ["ba̱x̱bog̱mgyemgn"]),
            ("-2PL.II", ["ba̱x̱bog̱mgyemksm"]),
            ("-3.II", ["ba̱x̱bog̱mgyemkt"]),
            ("[-3.II]=CN.IRR", ["ba̱x̱bog̱mgyemkł"]),
            ("[-3.II]=CN", ["ba̱x̱bog̱mgyemgi"]),
            ("[-3.II]=PN", ["ba̱x̱bog̱mgyemks"]),
            ("-SX", ["ba̱x̱bog̱mgyemgit"]),
            ("-ATTR", ["ba̱x̱bog̱mgyemgm", "ba̱x̱bog̱mgyemga"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_plainKW(self):
        stem = "w$a_t'ukw+N"
        expected_map = [
            ("", ["wa̱t'ukw"]),
            ("-1SG.II", ["wa̱t'ugwi", "wa̱t'ugwu"]),
            ("-1PL.II", ["wa̱t'ugwm"]),
            ("-2SG.II", ["wa̱t'ugwn"]),
            ("-2PL.II", ["wa̱t'ukwsm"]),
            ("-3.II", ["wa̱t'ukwt"]),
            ("[-3.II]=CN", ["wa̱t'ugwi"]),
            ("[-3.II]=CN.IRR", ["wa̱t'ukwł"]),
            ("[-3.II]=PN", ["wa̱t'ukws"]),
            ("-SX", ["wa̱t'ugwit"]),
            ("-ATTR", ["wa̱t'ugwm", "wa̱t'ugwa"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_plainX_(self):
        stem = "han$a_'a_x_+N"
        expected_map = [
            ("", ["hana̱'a̱x̱"]),
            ("-1SG.II", ["hana̱'a̱g̱ai", "hana̱'a̱g̱u"]),
            ("-1PL.II", ["hana̱'a̱g̱m"]),
            ("-2SG.II", ["hana̱'a̱g̱n"]),
            ("-2PL.II", ["hana̱'a̱x̱sm"]),
            ("-3.II", ["hana̱'a̱x̱t"]),
            ("[-3.II]=CN", ["hana̱'a̱g̱ai"]),
            ("[-3.II]=CN.IRR", ["hana̱'a̱x̱ł"]),
            ("[-3.II]=PN", ["hana̱'a̱x̱s"]),
            ("-SX", ["hana̱'a̱g̱it"]),
            ("-ATTR", ["hana̱'a̱g̱m", "hana̱'a̱g̱a"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)


@unittest.skip("need to convert to sgx")
class TestGlottalStops(TestFSTOutput):

    @classmethod
    def setUpClass(cls):
        test_stems = {
            "Noun": [
                "s$ip'",  # find a real glottal P
                "hl$it'",
                "n$aasik'",
                "ts'$uuts'",
                "giky'$otl'",
                "t'$ikw'",
                "han$ak_'",
                "ts'$ok_'",
            ]
        }
        super().setUpClass(FULL_SGX, test_stems)

    def test_glottP(self):
        stem = "s$ip'+N"
        expected_map = [
            ("-1SG.II", ["sip'i'y"]),
            ("-1PL.II", ["sip'i'm"]),
            ("-2SG.II", ["sip'in"]),
            ("-2PL.II", ["sip'si'm"]),
            ("-3.II", ["sip't"]),
            ("-3PL.II", ["sip'diit"]),
            ("[-3.II]=CN", ["sip'hl"]),
            ("[-3.II]=PN", ["sip's"]),
            ("-SX", ["sip'it"]),
            ("-ATTR", ["sip'im", "sip'a"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_glottT(self):
        stem = "hl$it'+N"
        expected_map = [
            ("-1SG.II", ["hlit'i'y"]),
            ("-1PL.II", ["hlit'i'm"]),
            ("-2SG.II", ["hlit'in"]),
            ("-2PL.II", ["hlit'si'm"]),
            ("-3.II", ["hlit't"]),
            ("-3PL.II", ["hlit'diit"]),
            ("[-3.II]=CN", ["hlit'hl"]),
            ("[-3.II]=PN", ["hlit's"]),
            ("-SX", ["hlit'it"]),
            ("-ATTR", ["hlit'im", "hlit'a"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_glottTS(self):
        stem = "ts'$uuts'+N"
        expected_map = [
            ("-1SG.II", ["ts'uuts'i'y"]),
            ("-1PL.II", ["ts'uuts'i'm"]),
            ("-2SG.II", ["ts'uuts'in"]),
            ("-2PL.II", ["ts'uuts'isi'm"]),  # ts'uuts'si'm?
            ("-3.II", ["ts'uuts't"]),
            ("-3PL.II", ["ts'uuts'diit"]),
            ("[-3.II]=CN", ["ts'uuts'hl"]),
            ("[-3.II]=PN", ["ts'uuts'"]),  # ts'uuts's?
            ("-SX", ["ts'uuts'it"]),
            ("-ATTR", ["ts'uuts'im", "ts'uuts'a"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_glottTL(self):
        stem = "giky'$otl'+N"
        expected_map = [
            ("-1SG.II", ["giky'otl'i'y"]),
            ("-1PL.II", ["giky'otl'i'm"]),
            ("-2SG.II", ["giky'otl'in"]),
            ("-2PL.II", ["giky'otl'si'm"]),
            ("-3.II", ["giky'otl't"]),
            ("-3PL.II", ["giky'otl'diit"]),
            ("[-3.II]=CN", ["giky'otl'hl"]),
            ("[-3.II]=PN", ["giky'otl's"]),
            ("-SX", ["giky'otl'it"]),
            ("-ATTR", ["giky'otl'im", "giky'otl'a"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_glottalK(self):
        stem = "n$aasik'+N"
        expected_map = [
            ("-1SG.II", ["naasik'i'y"]),
            ("-1PL.II", ["naasik'i'm"]),
            ("-2SG.II", ["naasik'in"]),
            ("-2PL.II", ["naasik'si'm"]),
            ("-3.II", ["naasik't"]),
            ("-3PL.II", ["naasik'diit"]),
            ("[-3.II]=CN", ["naasik'hl"]),
            ("[-3.II]=PN", ["naasik's"]),
            ("-SX", ["naasik'it"]),
            ("-ATTR", ["naasik'im", "naasik'a"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_glottKW(self):
        stem = "t'$ikw'+N"
        expected_map = [
            ("-1SG.II", ["t'ikw'i'y"]),
            ("-1PL.II", ["t'ikw'i'm", "t'ik'u'm"]),
            ("-2SG.II", ["t'ikw'in"]),
            ("-2PL.II", ["t'ikw'si'm"]),
            ("-3.II", ["t'ikw't"]),
            ("-3PL.II", ["t'ikw'diit"]),
            ("[-3.II]=CN", ["t'ikw'hl"]),
            ("[-3.II]=PN", ["t'ikw's"]),
            ("-SX", ["t'ikw'it"]),
            ("-ATTR", ["t'ikw'im", "t'ik'um", "t'ikw'a"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_glottK_(self):
        stem = "han$ak_'+N"
        expected_map = [
            ("-1SG.II", ["hanaḵ'a'y"]),
            ("-1PL.II", ["hanaḵ'a'm"]),
            ("-2SG.II", ["hanaḵ'an"]),
            ("-2PL.II", ["hanaḵ'si'm"]),
            ("-3.II", ["hanaḵ't"]),
            ("-3PL.II", ["hanaḵ'diit"]),
            ("[-3.II]=CN", ["hanaḵ'hl"]),
            ("[-3.II]=PN", ["hanaḵ's"]),
            ("-SX", ["hanaḵ'at"]),
            ("-ATTR", ["hanaḵ'am", "hanaḵ'a"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_glottOK_(self):
        stem = "ts'$ok_'+N"
        expected_map = [
            ("-1SG.II", ["ts'oḵ'a'y", "ts'oḵ'o'y"]),
            ("-1PL.II", ["ts'oḵ'a'm", "ts'oḵ'o'm"]),
            ("-2SG.II", ["ts'oḵ'on", "ts'oḵ'an"]),
            ("-2PL.II", ["ts'oḵ'si'm"]),
            ("-3.II", ["ts'oḵ't"]),
            ("-3PL.II", ["ts'oḵ'diit"]),
            ("[-3.II]=CN", ["ts'oḵ'hl"]),
            ("[-3.II]=PN", ["ts'oḵ's"]),
            ("-SX", ["ts'oḵ'at", "ts'oḵ'ot"]),
            ("-ATTR", ["ts'oḵ'am", "ts'oḵ'om", "ts'oḵ'a"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)


@unittest.skip("need to convert to sgx")
class TestFricatives(TestFSTOutput):

    @classmethod
    def setUpClass(cls):
        test_stems = {
            "Noun": [
                "m$aas",
                "k'$uuhl",
                "l$ax",
                "l$aaxw",
                "'n$ax_",
                "n$ox_",
            ]
        }
        super().setUpClass(FULL_SGX, test_stems)

    def test_fricS(self):
        stem = "m$aas+N"
        expected_map = [
            ("-1SG.II", ["maasi'y"]),
            ("-1PL.II", ["maasi'm"]),
            ("-2SG.II", ["maasin"]),
            ("-2PL.II", ["maasisi'm"]),
            ("-3.II", ["maast"]),
            ("-3PL.II", ["maasdiit"]),
            ("[-3.II]=CN", ["maashl"]),
            ("[-3.II]=PN", ["maas"]),
            ("-SX", ["maasit"]),
            ("-ATTR", ["maasim", "maasa"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_fricHL(self):
        stem = "k'$uuhl+N"
        expected_map = [
            ("-1SG.II", ["k'uuhli'y"]),
            ("-1PL.II", ["k'uuhli'm"]),
            ("-2SG.II", ["k'uuhlin"]),
            ("-2PL.II", ["k'uuhlsi'm"]),
            ("-3.II", ["k'uuhlt"]),
            ("-3PL.II", ["k'uuhldiit"]),
            ("[-3.II]=CN", ["k'uuhl"]),
            ("[-3.II]=PN", ["k'uuhls"]),
            ("-SX", ["k'uuhlit"]),
            ("-ATTR", ["k'uuhlim", "k'uuhla"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_fricX(self):
        stem = "l$ax+N"  # not sure if these should also be optionally glided
        expected_map = [
            ("-1SG.II", ["layi'y"]),
            ("-1PL.II", ["layi'm"]),
            ("-2SG.II", ["layin"]),
            ("-2PL.II", ["laxsi'm"]),
            ("-3.II", ["laxt"]),
            ("-3PL.II", ["laxdiit"]),
            ("[-3.II]=CN", ["laxhl"]),
            ("[-3.II]=PN", ["laxs"]),
            ("-SX", ["layit"]),
            ("-ATTR", ["layim", "laya"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_fricXW(self):
        stem = "l$aaxw+N"
        expected_map = [
            ("-1SG.II", ["laawi'y", "laaxwi'y"]),
            ("-1PL.II", ["laawi'm", "laawu'm", "laaxwi'm", "laaxu'm"]),
            ("-2SG.II", ["laawin", "laaxwin"]),
            ("-2PL.II", ["laaxwsi'm"]),
            ("-3.II", ["laaxwt"]),
            ("-3PL.II", ["laaxwdiit"]),
            ("[-3.II]=CN", ["laaxwhl"]),
            ("[-3.II]=PN", ["laaxws"]),
            ("-SX", ["laawit", "laaxwit"]),
            (
                "-ATTR",
                [
                    "laawim",
                    "laawum",
                    "laawa",
                    "laaxwim",
                    "laaxum",
                    "laaxwa",
                ],
            ),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_fricX_(self):
        stem = "'n$ax_+N"
        expected_map = [
            ("-1SG.II", ["'naha'y", "'nax̱a'y"]),
            ("-1PL.II", ["'naha'm", "'nax̱a'm"]),
            ("-2SG.II", ["'nahan", "'nax̱an"]),
            ("-2PL.II", ["'nax̱si'm"]),
            ("-3.II", ["'nax̱t"]),
            ("-3PL.II", ["'nax̱diit"]),
            ("[-3.II]=CN", ["'nax̱hl"]),
            ("[-3.II]=PN", ["'nax̱s"]),
            ("-SX", ["'nahat", "'nax̱at"]),
            ("-ATTR", ["'naham", "'naha", "'nax̱am", "'nax̱a"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_fricOX_(self):
        stem = "n$ox_+N"
        expected_map = [
            ("-1SG.II", ["noha'y", "noho'y", "nox̱a'y", "nox̱o'y"]),
            ("-1PL.II", ["noha'm", "noho'm", "nox̱a'm", "nox̱o'm"]),
            ("-2SG.II", ["nohan", "nohon", "nox̱an", "nox̱on"]),
            ("-2PL.II", ["nox̱si'm"]),
            ("-3.II", ["nox̱t"]),
            ("-3PL.II", ["nox̱diit"]),
            ("[-3.II]=CN", ["nox̱hl"]),
            ("[-3.II]=PN", ["nox̱s"]),
            ("-SX", ["nohat", "nohot", "nox̱at", "nox̱ot"]),
            ("-ATTR", ["noham", "nohom", "noha", "nox̱am", "nox̱om", "nox̱a"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)


@unittest.skip("need to convert to sgx")
class TestPlainSonorants(TestFSTOutput):

    @classmethod
    def setUpClass(cls):
        test_stems = {
            "Noun": [
                "g$um",
                "b$an",
                "haw$il",
                "g_awk_'$aw",
                # "y",
            ]
        }
        super().setUpClass(FULL_SGX, test_stems)

    def test_plainM(self):
        stem = "g$um+N"
        expected_map = [
            ("-1SG.II", ["gumi'y"]),
            ("-1PL.II", ["gumi'm", "gumu'm"]),
            ("-2SG.II", ["gumin"]),
            ("-2PL.II", ["gumsi'm"]),
            ("-3.II", ["gumt"]),
            ("-3PL.II", ["gumdiit"]),
            ("[-3.II]=CN", ["gumhl"]),
            ("[-3.II]=PN", ["gums"]),
            ("-SX", ["gumit", "gumt"]),
            ("-ATTR", ["gumim", "gumum", "guma"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_plainN(self):
        stem = "b$an+N"
        expected_map = [
            ("-1SG.II", ["bani'y"]),
            ("-1PL.II", ["bani'm"]),
            ("-2SG.II", ["banin"]),
            ("-2PL.II", ["bansi'm"]),
            ("-3.II", ["bant"]),
            ("-3PL.II", ["bandiit"]),
            ("[-3.II]=CN", ["banhl"]),
            ("[-3.II]=PN", ["bans"]),
            ("-SX", ["banit", "bant"]),
            ("-ATTR", ["banim", "bana"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_plainL(self):
        stem = "haw$il+N"
        expected_map = [
            ("-1SG.II", ["hawili'y"]),
            ("-1PL.II", ["hawili'm"]),
            ("-2SG.II", ["hawilin"]),
            ("-2PL.II", ["hawilsi'm"]),
            ("-3.II", ["hawilt"]),
            ("-3PL.II", ["hawildiit"]),
            ("[-3.II]=CN", ["hawilhl"]),
            ("[-3.II]=PN", ["hawils"]),
            ("-SX", ["hawilit", "hawilt"]),  # hawilt? hawilit?
            ("-ATTR", ["hawilim", "hawila"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_plainW(self):
        stem = "g_awk_'$aw+N"
        expected_map = [
            ("-1SG.II", ["g̱awḵ'awi'y"]),
            ("-1PL.II", ["g̱awḵ'awi'm", "g̱awḵ'awu'm"]),
            ("-2SG.II", ["g̱awḵ'awin"]),
            ("-2PL.II", ["g̱awḵ'awsi'm"]),
            ("-3.II", ["g̱awḵ'awt"]),
            ("-3PL.II", ["g̱awḵ'awdiit"]),
            ("[-3.II]=CN", ["g̱awḵ'awhl"]),
            ("[-3.II]=PN", ["g̱awḵ'aws"]),
            ("-SX", ["g̱awḵ'awit", "g̱awḵ'awt"]),
            ("-ATTR", ["g̱awḵ'awim", "g̱awḵ'awum", "g̱awḵ'awa"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)


@unittest.skip("need to convert to sgx")
class TestGlottalSonorants(TestFSTOutput):

    @classmethod
    def setUpClass(cls):
        test_stems = {
            "Noun": [
                "hl$aa'm",
                "lig$i'l",
                "mask_'ay$aa'y",
                "x_b$aa'w",
                "n$oo'o",
                # "ba'n",
            ]
        }
        super().setUpClass(FULL_SGX, test_stems)

    def test_glottalM(self):
        stem = "hl$aa'm+N"
        expected_map = [
            ("-1SG.II", ["hlaa'mi'y"]),
            # ('-1PL.II',    ["hlaa'mi'm", "hlaa'mm"]), # ??
            ("-2SG.II", ["hlaa'min"]),
            ("-2PL.II", ["hlaa'msi'm"]),
            ("-3.II", ["hlaa'mt"]),
            ("-3PL.II", ["hlaa'mdiit"]),
            ("[-3.II]=CN", ["hlaa'mhl"]),
            ("[-3.II]=PN", ["hlaa'ms"]),
            ("-SX", ["hlaa'mit"]),  # ??
            ("-ATTR", ["hlaa'mim", "hlaa'ma"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    #     def test_glottalN(self):
    #         stem = "b$an+N"
    #         expected_map = [
    #             ('-1SG.II',    ["bani'y"]),
    #             ('-1PL.II',    ["bani'm"]),
    #             ('-2SG.II',    ["banin"]),
    #             ('-2PL.II',    ["bansi'm"]),
    #             ('-3.II',      ["bant"]),
    #             ('-3PL.II',    ["bandiit"]),
    #             ('[-3.II]=CN',   ["banhl"]),
    #             ('[-3.II]=PN',   ["bans"]),
    #             ('-SX',     ["bant"]),
    #             ('-ATTR',   ["banim", "bana"]),
    #         ]
    #         for gloss, expected_forms in expected_map:
    #             result_list = self.fst.generate(stem+gloss)
    #             for form in expected_forms:
    #                 with self.subTest(form=stem+gloss):
    #                     self.assertIn(form, result_list)
    #             self.assertEqual(len(result_list), len(expected_forms),
    #                 "{} should have {} results".format(stem+gloss,
    # len(expected_forms)))

    def test_glottalL(self):
        stem = "lig$i'l+N"
        expected_map = [
            ("-1SG.II", ["ligi'li'y"]),
            ("-1PL.II", ["ligi'li'm"]),
            ("-2SG.II", ["ligi'lin"]),
            ("-2PL.II", ["ligi'lsi'm"]),
            ("-3.II", ["ligi'lt"]),
            ("-3PL.II", ["ligi'ldiit"]),
            ("[-3.II]=CN", ["ligi'lhl"]),
            ("[-3.II]=PN", ["ligi'ls"]),
            ("-SX", ["ligi'lit"]),
            ("-ATTR", ["ligi'lim", "ligi'la"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_glottalY(self):
        stem = "mask_'ay$aa'y+N"
        expected_map = [
            ("-1SG.II", ["masḵ'ayaa'y"]),  # ??
            ("-1PL.II", ["masḵ'ayaa'yi'm"]),
            ("-2SG.II", ["masḵ'ayaa'yin"]),
            ("-2PL.II", ["masḵ'ayaa'ysi'm"]),
            ("-3.II", ["masḵ'ayaa'yt"]),
            ("-3PL.II", ["masḵ'ayaa'ydiit"]),
            ("[-3.II]=CN", ["masḵ'ayaa'yhl"]),
            ("[-3.II]=PN", ["masḵ'ayaa'ys"]),
            ("-SX", ["masḵ'ayaa'yit"]),
            ("-ATTR", ["masḵ'ayaa'yim", "masḵ'ayaa'ya"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_glottalW(self):
        stem = "x_b$aa'w+N"
        expected_map = [
            ("-1SG.II", ["x̱baa'wi'y"]),
            ("-1PL.II", ["x̱baa'wi'm", "x̱baa'u'm"]),
            ("-2SG.II", ["x̱baa'win"]),
            ("-2PL.II", ["x̱baa'wsi'm"]),
            ("-3.II", ["x̱baa'wt"]),
            ("-3PL.II", ["x̱baa'wdiit"]),
            ("[-3.II]=CN", ["x̱baa'whl"]),
            ("[-3.II]=PN", ["x̱baa'ws"]),
            # ('-SX',     ["x̱baa'wit", "x̱baa'ut"]),
            # haven't applied this yet, keep in mind
            ("-ATTR", ["x̱baa'wim", "x̱baa'um", "x̱baa'wa"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_glottalStop(self):
        stem = "n$oo'o+N"
        expected_map = [
            ("-1SG.II", ["noo'o'y"]),
            ("-1PL.II", ["noo'o'm"]),
            ("-2SG.II", ["noo'on"]),
            ("-2PL.II", ["noo'osi'm"]),
            ("-3.II", ["noo'ot"]),
            ("-3PL.II", ["noo'odiit"]),
            ("[-3.II]=CN", ["noo'ohl"]),
            ("[-3.II]=PN", ["noo'os"]),
            ("-SX", ["noo'ot"]),
            ("-ATTR", ["noo'om", "noo'a"]),  # ??
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)


@unittest.skip("need to convert to sgx")
class TestVowels(TestFSTOutput):

    @classmethod
    def setUpClass(cls):
        test_stems = {
            "Noun": [
                "w$a",
                "ha'niig$ilbilsa",
                "gy$uu",
                "majag_al$ee",
                "k_'$esii",
            ],
            "IntransitiveVerb": ["y$ee"],
        }
        super().setUpClass(FULL_SGX, test_stems)

    def test_shortA(self):
        stem = "w$a+N"
        expected_map = [
            ("-1SG.II", ["wa'y"]),
            ("-1PL.II", ["wa'm"]),
            ("-2SG.II", ["wan"]),
            ("-2PL.II", ["wasi'm"]),
            ("-3.II", ["wat"]),
            ("-3PL.II", ["wadiit"]),
            ("[-3.II]=CN", ["wahl"]),
            ("[-3.II]=PN", ["was"]),
            ("-SX", ["wat"]),
            ("-ATTR", ["wam", "waha"]),  # ??
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_shortAlonger(self):
        stem = "ha'niig$ilbilsa+N"
        expected_map = [
            ("-1SG.II", ["ha'niigilbilsa'y"]),
            ("-1PL.II", ["ha'niigilbilsa'm"]),
            ("-2SG.II", ["ha'niigilbilsan"]),
            ("-2PL.II", ["ha'niigilbilsasi'm"]),
            ("-3.II", ["ha'niigilbilsat"]),
            ("-3PL.II", ["ha'niigilbilsadiit"]),
            ("[-3.II]=CN", ["ha'niigilbilsahl"]),
            ("[-3.II]=PN", ["ha'niigilbilsas"]),
            ("-SX", ["ha'niigilbilsat"]),
            ("-ATTR", ["ha'niigilbilsam", "ha'niigilbilsaha"]),  # ??
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_longU(self):
        stem = "gy$uu+N"
        expected_map = [
            ("-1SG.II", ["gyuu'y"]),
            ("-1PL.II", ["gyuu'm"]),
            ("-2SG.II", ["gyuun"]),
            ("-2PL.II", ["gyuusi'm"]),
            ("-3.II", ["gyuut"]),
            ("-3PL.II", ["gyuudiit"]),
            ("[-3.II]=CN", ["gyuuhl"]),
            ("[-3.II]=PN", ["gyuus"]),
            ("-SX", ["gyuut"]),
            ("-ATTR", ["gyuum", "gyuuha"]),  # ??
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_longE(self):
        stem = "y$ee+VI"
        expected_map = [
            ("-1SG.II", ["yee'y"]),
            ("-1PL.II", ["yee'm"]),
            # ('-2SG.II',    ["yeen", "yin"]), # requires maximal parser
            ("-2PL.II", ["yeesi'm"]),
            ("-3.II", ["yeet"]),
            ("[-3.II]=CN", ["yeehl"]),
            ("[-3.II]=PN", ["yees"]),
            ("-SX", ["yeet"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_longElonger(self):
        stem = "majag_al$ee+N"
        expected_map = [
            ("-1SG.II", ["majag̱alee'y"]),
            ("-1PL.II", ["majag̱alee'm"]),
            ("-2SG.II", ["majag̱aleen"]),
            ("-2PL.II", ["majag̱aleesi'm"]),
            ("-3.II", ["majag̱aleet"]),
            ("-3PL.II", ["majag̱aleediit"]),
            ("[-3.II]=CN", ["majag̱aleehl"]),
            ("[-3.II]=PN", ["majag̱alees"]),
            ("-SX", ["majag̱aleet"]),
            ("-ATTR", ["majag̱aleem", "majag̱aleeha"]),  # ??
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_longI(self):
        stem = "k_'$esii+N"
        expected_map = [
            ("-1SG.II", ["ḵ'esii'y"]),
            ("-1PL.II", ["ḵ'esii'm"]),
            ("-2SG.II", ["ḵ'esiin"]),
            ("-2PL.II", ["ḵ'esiisi'm"]),
            ("-3.II", ["ḵ'esiit"]),
            ("-3PL.II", ["ḵ'esiidiit"]),
            ("[-3.II]=CN", ["ḵ'esiihl"]),
            ("[-3.II]=PN", ["ḵ'esiis"]),
            ("-SX", ["ḵ'esiit"]),
            ("-ATTR", ["ḵ'esiim", "ḵ'esiiha"]),  # ??
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)


@unittest.skip("need to convert to sgx")
class TestClusters(TestFSTOutput):

    @classmethod
    def setUpClass(cls):
        test_stems = {
            "Noun": [
                "x_b$iist",  # non-T
                "hal$ayt",
                "w$ilp",
                "s$ilkw",
                "ts'$amtx",
                "'$ax_xw",
                "biy$oosxw",
                "h$upx_",
            ]
        }
        super().setUpClass(FULL_SGX, test_stems)

    def test_ST(self):
        stem = "x_b$iist+N"
        expected_map = [
            ("-1SG.II", ["x̱biisdi'y"]),
            ("-1PL.II", ["x̱biisdi'm"]),
            ("-2SG.II", ["x̱biisdin"]),
            ("-2PL.II", ["x̱biistsi'm"]),
            ("-3.II", ["x̱biistt"]),
            ("-3PL.II", ["x̱biistdiit"]),
            ("[-3.II]=CN", ["x̱biisthl"]),
            ("[-3.II]=PN", ["x̱biists"]),
            ("-SX", ["x̱biisdit"]),
            ("-ATTR", ["x̱biisdim", "x̱biisda"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_YT(self):
        stem = "hal$ayt+N"
        expected_map = [
            ("-1SG.II", ["halaydi'y"]),
            ("-1PL.II", ["halaydi'm"]),
            ("-2SG.II", ["halaydin"]),
            ("-2PL.II", ["halaytsi'm"]),
            ("-3.II", ["halaytt"]),
            ("-3PL.II", ["halaytdiit"]),
            ("[-3.II]=CN", ["halaythl"]),
            ("[-3.II]=PN", ["halayts"]),
            ("-SX", ["halaydit"]),
            ("-ATTR", ["halaydim", "halayda"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_LP(self):
        stem = "w$ilp+N"
        expected_map = [
            ("-1SG.II", ["wilbi'y"]),
            ("-1PL.II", ["wilbi'm"]),
            ("-2SG.II", ["wilbin"]),
            ("-2PL.II", ["wilpsi'm"]),
            ("-3.II", ["wilpt"]),
            ("-3PL.II", ["wilpdiit"]),
            ("[-3.II]=CN", ["wilphl"]),
            ("[-3.II]=PN", ["wilps"]),
            ("-SX", ["wilbit"]),
            ("-ATTR", ["wilbim", "wilba"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_LKW(self):
        stem = "s$ilkw+N"
        expected_map = [
            ("-1SG.II", ["silgwi'y"]),
            ("-1PL.II", ["silgwi'm", "silgu'm"]),
            ("-2SG.II", ["silgwin"]),
            ("-2PL.II", ["silkwsi'm"]),
            ("-3.II", ["silkwt"]),
            ("-3PL.II", ["silkwdiit"]),
            ("[-3.II]=CN", ["silkwhl"]),
            ("[-3.II]=PN", ["silkws"]),
            ("-SX", ["silgwit"]),
            ("-ATTR", ["silgwim", "silgum", "silgwa"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_TX(self):
        stem = "ts'$amtx+N"
        expected_map = [
            ("-1SG.II", ["ts'amtxi'y"]),
            ("-1PL.II", ["ts'amtxi'm"]),
            ("-2SG.II", ["ts'amtxin"]),
            ("-2PL.II", ["ts'amtxsi'm"]),
            ("-3.II", ["ts'amtxt"]),
            ("-3PL.II", ["ts'amtxdiit"]),
            ("[-3.II]=CN", ["ts'amtxhl"]),
            ("[-3.II]=PN", ["ts'amtxs"]),
            ("-SX", ["ts'amtxit"]),
            ("-ATTR", ["ts'amtxim", "ts'amtxa"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_SXW(self):
        stem = "biy$oosxw+N"
        expected_map = [
            ("-1SG.II", ["biyoosxwi'y"]),
            ("-1PL.II", ["biyoosxwi'm", "biyoosxu'm"]),
            ("-2SG.II", ["biyoosxwin"]),
            ("-2PL.II", ["biyoosxwsi'm"]),
            ("-3.II", ["biyoosxwt"]),
            ("-3PL.II", ["biyoosxwdiit"]),
            ("[-3.II]=CN", ["biyoosxwhl"]),
            ("[-3.II]=PN", ["biyoosxws"]),
            ("-SX", ["biyoosxwit"]),
            ("-ATTR", ["biyoosxwim", "biyoosxum", "biyoosxwa"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_X_XW(self):
        stem = "'$ax_xw+N"
        expected_map = [
            ("-1SG.II", ["ax̱xwi'y"]),
            ("-1PL.II", ["ax̱xwi'm", "ax̱xu'm"]),
            ("-2SG.II", ["ax̱xwin"]),
            ("-2PL.II", ["ax̱xwsi'm"]),
            ("-3.II", ["ax̱xwt"]),
            ("-3PL.II", ["ax̱xwdiit"]),
            ("[-3.II]=CN", ["ax̱xwhl"]),
            ("[-3.II]=PN", ["ax̱xws"]),
            ("-SX", ["ax̱xwit"]),
            ("-ATTR", ["ax̱xwim", "ax̱xum", "ax̱xwa"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_PX_(self):
        stem = "h$upx_+N"
        expected_map = [
            ("-1SG.II", ["hupx̱a'y"]),
            ("-1PL.II", ["hupx̱a'm"]),
            ("-2SG.II", ["hupx̱an"]),
            ("-2PL.II", ["hupx̱si'm"]),
            ("-3.II", ["hupx̱t"]),
            ("-3PL.II", ["hupx̱diit"]),
            ("[-3.II]=CN", ["hupx̱hl"]),
            ("[-3.II]=PN", ["hupx̱s"]),
            ("-SX", ["hupx̱at"]),
            ("-ATTR", ["hupx̱am", "hupx̱a"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)


if __name__ == "__main__":
    unittest.main()

# python -m unittest test
# python -m unittest discover # all test files in current dir
# python -m unittest discover -s tests # all test files in /tests
