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
                "ł$ik'ots",
                "nts'$i'its", 
                "b$a_x_bog_mgyemk",
                "w$a_t'ukw",
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
            # ("-SX", ["chaybit"]),
            ("-ATTR", ["chaybm"]),
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
            # ("-SX", ["g̱oodit"]),
            ("-ATTR", ["g̱oodm"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_plainTS(self):
        stem = "ł$ik'ots+N"
        expected_map = [
            ("", ["łik'ots"]),
            ("-1SG.II", ["łik'odzi", "łik'odzu"]),
            ("-1PL.II", ["łik'odzm"]),
            ("-2SG.II", ["łik'odzn"]),
            ("-2PL.II", ["łik'odzism"]),
            ("-3.II", ["łik'otst"]),
            ("[-3.II]=CN.IRR", ["łik'otsł"]),
            ("[-3.II]=CN", ["łik'odzi"]),
            ("[-3.II]=PN", ["łik'ots"]),
            # ("-SX", ["łik'odzit"]),
            ("-ATTR", ["łik'odzm"]),
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
            # ("-SX", ["ba̱x̱bog̱mgyemgit"]),
            ("-ATTR", ["ba̱x̱bog̱mgyemgm"]),
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
            # ("-SX", ["wa̱t'ugwit"]),
            ("-ATTR", ["wa̱t'ugwm"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    
class TestFricatives(TestFSTOutput):

    @classmethod
    def setUpClass(cls):
        test_stems = {
            "Noun": [
                "d$uus",
                "n$o'oł",
                "ts'mm$üüx",
                "'y$axw",
                "an$aaxy",
                "$aax_",
            ]
        }
        super().setUpClass(FULL_SGX, test_stems)

    def test_fricS(self):
        stem = "d$uus+N"
        expected_map = [
            ("", ["duus"]),
            ("-1SG.II", ["duusi", "duusu"]),
            ("-1PL.II", ["duusm"]),
            ("-2SG.II", ["duusn"]),
            ("-2PL.II", ["duusism"]),
            ("-3.II", ["duust"]),
            ("[-3.II]=CN", ["duusi"]),
            ("[-3.II]=CN.IRR", ["duusł"]),
            ("[-3.II]=PN", ["duus"]),
            # ("-SX", ["duusit"]),
            ("-ATTR", ["duusm"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_fricHL(self):
        # NOTE: this is not a glottal coda, so the apostrophe should stay fixed
        stem = "n$o'oł+N"
        expected_map = [
            ("", ["no'oł"]),
            ("-1SG.II", ["no'ołi", "no'ołu"]),
            ("-1PL.II", ["no'ołm"]),
            ("-2SG.II", ["no'ołn"]),
            ("-2PL.II", ["no'ołsm"]),
            ("-3.II", ["no'ołt"]),
            ("[-3.II]=CN", ["no'ołi"]),
            ("[-3.II]=CN.IRR", ["no'oł"]),
            ("[-3.II]=PN", ["no'ołs"]),
            # ("-SX", ["no'ołit"]),
            ("-ATTR", ["no'ołm"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_fricX(self):
        stem = "ts'mm$üüx+N"
        expected_map = [
            ("", ["ts'mmüüx"]),
            ("-1SG.II", ["ts'mmüüxi", "ts'mmüüxu"]),
            ("-1PL.II", ["ts'mmüüxm"]),
            ("-2SG.II", ["ts'mmüüxn"]),
            ("-2PL.II", ["ts'mmüüxsm"]),
            ("-3.II", ["ts'mmüüxt"]),
            ("[-3.II]=CN", ["ts'mmüüxi"]),
            ("[-3.II]=CN.IRR", ["ts'mmüüxł"]),
            ("[-3.II]=PN", ["ts'mmüüxs"]),
            # ("-SX", ["ts'mmüüxit"]),
            ("-ATTR", ["ts'mmüüxm"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_fricXW(self):
        stem = "'y$axw+N"
        expected_map = [
            ("", ["'yaxw"]),
            ("-1SG.II", ["'yaxwi", "'yaxwu"]),
            ("-1PL.II", ["'yaxwm"]),
            ("-2SG.II", ["'yaxwn"]),
            ("-2PL.II", ["'yaxwsm"]),
            ("-3.II", ["'yaxwt"]),
            ("[-3.II]=CN", ["'yaxwi"]),
            ("[-3.II]=CN.IRR", ["'yaxwł"]),
            ("[-3.II]=PN", ["'yaxws"]),
            # ("-SX", ["'yaxwit"]),
            ("-ATTR", ["'yaxwm"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_fricXY(self):
        stem = "an$aaxy+N"
        expected_map = [
            ("", ["anaaxy"]),
            ("-1SG.II", ["anaaxyi", "anaaxyu"]),
            ("-1PL.II", ["anaaxym"]),
            ("-2SG.II", ["anaaxyn"]),
            ("-2PL.II", ["anaaxysm"]),
            ("-3.II", ["anaaxyt"]),
            ("[-3.II]=CN", ["anaaxyi"]),
            ("[-3.II]=CN.IRR", ["anaaxył"]),
            ("[-3.II]=PN", ["anaaxys"]),
            # ("-SX", ["anaaxyit"]),
            ("-ATTR", ["anaaxym"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_fricOX_(self):
        stem = "$aax_+N"
        expected_map = [
            ("", ["aax̱"]),
            ("-1SG.II", ["aag̱ai", "aag̱u"]),
            ("-1PL.II", ["aag̱m"]),
            ("-2SG.II", ["aag̱n"]),
            ("-2PL.II", ["aax̱sm"]),
            ("-3.II", ["aax̱t"]),
            ("[-3.II]=CN", ["aag̱ai"]),
            ("[-3.II]=CN.IRR", ["aax̱ł"]),
            ("[-3.II]=PN", ["aax̱s"]),
            # ("-SX", ["aag̱at"]),
            ("-ATTR", ["aag̱m"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

class TestPlainSonorants(TestFSTOutput):

    @classmethod
    def setUpClass(cls):
        test_stems = {
            "Noun": [
                "'w$aan",
                "g$oom",
                "k_'awk_'$aw",
                "amh$aẅ",
                "łgwisg_$ay",
            ]
        }
        super().setUpClass(FULL_SGX, test_stems)

    def test_plainN(self):
        stem = "'w$aan+N"
        expected_map = [
            ("", ["'waan"]),
            ("-1SG.II", ["'waani", "'waanu"]),
            ("-1PL.II", ["'waanm"]),
            ("-2SG.II", ["'waan"]),
            ("-2PL.II", ["'waansm"]),
            ("-3.II", ["'waant"]),
            ("[-3.II]=CN", ["'waani"]),
            ("[-3.II]=CN.IRR", ["'waanł"]),
            ("[-3.II]=PN", ["'waans"]),
            # ("-SX", ["'waanit", "'waant"]),
            ("-ATTR", ["'waanm"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_plainM(self):
        stem = "g$oom+N"
        expected_map = [
            ("", ["goom"]),
            ("-1SG.II", ["goomi", "goomu"]),
            ("-1PL.II", ["goomim"]),
            ("-2SG.II", ["goomn"]),
            ("-2PL.II", ["goomsm"]),
            ("-3.II", ["goomt"]),
            ("[-3.II]=CN", ["goomi"]),
            ("[-3.II]=CN.IRR", ["goomł"]),
            ("[-3.II]=PN", ["gooms"]),
            # ("-SX", ["goomit", "goomt"]),
            ("-ATTR", ["goomim"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_plainW(self):
        stem = "k_'awk_'$aw+N"
        expected_map = [
            ("", ["ḵ'awḵ'aw"]),
            ("-1SG.II", ["ḵ'awḵ'awi", "ḵ'awḵ'awu"]),
            ("-1PL.II", ["ḵ'awḵ'awm"]),
            ("-2SG.II", ["ḵ'awḵ'awn"]),
            ("-2PL.II", ["ḵ'awḵ'awsm"]),
            ("-3.II", ["ḵ'awḵ'awt"]),
            ("[-3.II]=CN", ["ḵ'awḵ'awi"]),
            ("[-3.II]=CN.IRR", ["ḵ'awḵ'awł"]),
            ("[-3.II]=PN", ["ḵ'awḵ'aws"]),
            # ("-SX", ["ḵ'awḵ'awit", "ḵ'awḵ'awt"]),
            ("-ATTR", ["ḵ'awḵ'awm"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_plainWeirdW(self):
        stem = "amh$aẅ+N"
        expected_map = [
            ("", ["amhaẅ"]),
            ("-1SG.II", ["amhaẅi", "amhaẅu"]),
            ("-1PL.II", ["amhaẅm"]),
            ("-2SG.II", ["amhaẅn"]),
            ("-2PL.II", ["amhaẅsm"]),
            ("-3.II", ["amhaẅt"]),
            ("[-3.II]=CN.IRR", ["amhaẅł"]),
            ("[-3.II]=CN", ["amhaẅi"]),
            ("[-3.II]=PN", ["amhaẅs"]),
            # ("-SX", ["amhaẅit", "amhaẅt"]), 
            ("-ATTR", ["amhaẅm"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_plainY(self):
        stem = "łgwisg_$ay+N"
        expected_map = [
            ("", ["łgwisg̱ay"]),
            ("-1SG.II", ["łgwisg̱ayi", "łgwisg̱ayu"]),
            ("-1PL.II", ["łgwisg̱aym"]),
            ("-2SG.II", ["łgwisg̱ayn"]),
            ("-2PL.II", ["łgwisg̱aysm"]),
            ("-3.II", ["łgwisg̱ayt"]),
            ("[-3.II]=CN", ["łgwisg̱ayi"]),
            ("[-3.II]=CN.IRR", ["łgwisg̱aył"]),
            ("[-3.II]=PN", ["łgwisg̱ays"]),
            # ("-SX", ["łgwisg̱ayit"]),
            ("-ATTR", ["łgwisg̱aym"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)


class TestGlottalCoda(TestFSTOutput):

    @classmethod
    def setUpClass(cls):
        test_stems = {
            "Noun": [
                # add 'p
                "ł$a'at",
                "nts'$i'its",
                "han$a'ax_",

                # sonorants
                "łił$a'am",
                "m$o'on",
                "lagy$i'il",
                "m$a'ay",
                "kp$a'aw",
                "ts'$ila'a",
                "ts'$ila_'a_"
            ]
        }
        super().setUpClass(FULL_SGX, test_stems)

    def test_glottT(self):
        stem = "ł$a'at+N"
        expected_map = [
            ("", ["ła'at", "ła't", "łaa't"]),
            ("-1SG.II", ["ła'adi", "ła'di", "łaa'di", "ła'adu", "ła'du", "łaa'du"]),
            ("-1PL.II", ["ła'adm", "ła'dm", "łaa'dm"]),
            ("-2SG.II", ["ła'adn", "ła'dn", "łaa'dn"]),
            ("-2PL.II", ["ła'atsm", "ła'tsm", "łaa'tsm"]),
            ("-3.II", ["ła'at", "ła't", "łaa't"]),
            ("[-3.II]=CN", ["ła'adi", "ła'di", "łaa'di"]),
            ("[-3.II]=CN.IRR", ["ła'atł", "ła'tł", "łaa'tł"]),
            ("[-3.II]=PN", ["ła'ats", "ła'ts", "łaa'ts"]),
            # ("-SX", ["ła'adit", "ła'dit", "łaa'dit"]),
            ("-ATTR", ["ła'adm", "ła'dm", "łaa'dm"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_glottTS(self):
        stem = "nts'$i'its+N"
        expected_map = [
            ("", ["nts'ii'ts"]),
            ("-1SG.II", ["nts'i'itsi", "nts'ii'tsi", "nts'i'tsi", "nts'i'idzi", "nts'ii'dzi", "nts'i'dzi", "nts'i'itsu", "nts'ii'tsu", "nts'i'tsu", "nts'i'idzu", "nts'ii'dzu", "nts'i'dzu"]),
            ("-1PL.II", ["nts'i'itsm", "nts'ii'tsm", "nts'i'tsm", "nts'i'idzm", "nts'ii'dzm", "nts'i'dzm"]),
            ("-2SG.II", ["nts'i'itsn", "nts'ii'tsn", "nts'i'tsn", "nts'i'idzn", "nts'ii'dzn", "nts'i'dzn"]),
            ("-2PL.II", ["nts'i'itsism", "nts'ii'tsism", "nts'i'tsism", "nts'i'idzism", "nts'ii'dzism", "nts'i'dzism"]),
            ("-3.II", ["nts'i'itst", "nts'ii'tst", "nts'i'tst"]),
            ("[-3.II]=CN", ["nts'i'itsi", "nts'ii'tsi", "nts'i'tsi", "nts'i'idzi", "nts'ii'dzi", "nts'i'dzi"]),
            ("[-3.II]=CN.IRR", ["nts'i'itsł", "nts'ii'tsł", "nts'i'tsł"]),
            ("[-3.II]=PN", ["nts'i'its", "nts'ii'ts", "nts'i'ts"]),
            # ("-SX", ["nts'i'itsit", "nts'ii'tsit", "nts'i'tsit", "nts'i'idzit", "nts'ii'dzit", "nts'i'dzit"]),
            ("-ATTR", ["nts'i'itsm", "nts'ii'tsm", "nts'i'tsm", "nts'i'idzm", "nts'ii'dzm", "nts'i'dzm"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    @unittest.skip("need to combine with below test results")
    def test_glottK_(self):
        stem = "han$a'k_+N"
        expected_map = [
            ("", ["hana'ḵ"]),
            ("-1SG.II", ["hana'g̱ai", "hana'g̱u"]),
            ("-1PL.II", ["hana'g̱m"]),
            ("-2SG.II", ["hana'g̱n"]),
            ("-2PL.II", ["hana'ḵsm"]),
            ("-3.II", ["hana'ḵt"]),
            ("[-3.II]=CN", ["hana'g̱ai"]),
            ("[-3.II]=CN.IRR", ["hana'ḵł"]), 
            ("[-3.II]=PN", ["hana'ḵs"]),
            # ("-SX", ["hana'g̱at"]),
            ("-ATTR", ["hana'g̱m"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)
        
    @unittest.skip("need to convert to new glottal variation behavior")
    def test_glottX_(self):
        stem = "han$a'ax_+N"
        expected_map = [
            ("", ["hana'ax̱"]),
            ("-1SG.II", ["hana'ag̱ai", "hana'ag̱u"]),
            ("-1PL.II", ["hana'ag̱m"]),
            ("-2SG.II", ["hana'ag̱n"]),
            ("-2PL.II", ["hana'ax̱sm"]),
            ("-3.II", ["hana'ax̱t"]),
            ("[-3.II]=CN", ["hana'ag̱ai"]),
            ("[-3.II]=CN.IRR", ["hana'ax̱ł"]),
            ("[-3.II]=PN", ["hana'ax̱s"]),
            # ("-SX", ["hana'ag̱at"]),
            ("-ATTR", ["hana'ag̱m"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    @unittest.skip("need to convert to new glottal variation behavior")
    def test_glottalM(self):
        stem = "łił$a'am+N"
        expected_map = [
            ("", ["łiła'am"]),
            ("-1SG.II", ["łiła'amu", "łiła'ami"]),
            ('-1PL.II',    ["łiła'amim"]), 
            ("-2SG.II", ["łiła'amn"]),
            ("-2PL.II", ["łiła'amsm"]),
            ("-3.II", ["łiła'amt"]),
            ("[-3.II]=CN", ["łiła'ami"]),
            ("[-3.II]=CN.IRR", ["łiła'amł"]),
            ("[-3.II]=PN", ["łiła'ams"]),
            # ("-SX", ["łiła'amit"]),  
            ("-ATTR", ["łiła'amim"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    @unittest.skip("need to convert to new glottal variation behavior")
    def test_glottalN(self):
        stem = "m$o'on+N"
        expected_map = [
            ("", ["mo'on"]),
            ("-1SG.II", ["mo'onu", "mo'oni"]),
            ('-1PL.II',    ["mo'onm"]), 
            ("-2SG.II", ["mo'on"]),
            ("-2PL.II", ["mo'onsm"]),
            ("-3.II", ["mo'ont"]),
            ("[-3.II]=CN", ["mo'oni"]),
            ("[-3.II]=CN.IRR", ["mo'onł"]),
            ("[-3.II]=PN", ["mo'ons"]),
            # ("-SX", ["mo'onit"]),  
            ("-ATTR", ["mo'onm"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    @unittest.skip("need to convert to new glottal variation behavior")
    def test_glottalL(self):
        stem = "lagy$i'il+N"
        expected_map = [
            ("", ["lagyi'il"]),
            ("-1SG.II", ["lagyi'ili", "lagyi'ilu",]),
            ("-1PL.II", ["lagyi'ilm"]),
            ("-2SG.II", ["lagyi'iln"]),
            ("-2PL.II", ["lagyi'ilsm"]),
            ("-3.II", ["lagyi'ilt"]),
            ("[-3.II]=CN", ["lagyi'ili"]),
            ("[-3.II]=CN.IRR", ["lagyi'ilł", "lagyi'ił"]),
            ("[-3.II]=PN", ["lagyi'ils"]),
            # ("-SX", ["lagyi'ilit"]),
            ("-ATTR", ["lagyi'ilm"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    @unittest.skip("need to combine with above test results")
    def test_glottalLShort(self):
        stem = "lagy$i'l+N"
        expected_map = [
            ("", ["lagyi'l"]),
            ("-1SG.II", ["lagyi'li", "lagyi'lu",]),
            ("-1PL.II", ["lagyi'lm"]),
            ("-2SG.II", ["lagyi'ln"]),
            ("-2PL.II", ["lagyi'lsm"]),
            ("-3.II", ["lagyi'lt"]),
            ("[-3.II]=CN", ["lagyi'li"]),
            ("[-3.II]=CN.IRR", ["lagyi'lł", "lagyi'ł"]),
            ("[-3.II]=PN", ["lagyi'ls"]),
            # ("-SX", ["lagyi'lit"]),
            ("-ATTR", ["lagyi'lm"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    @unittest.skip("need to convert to new glottal variation behavior")
    def test_glottalY(self):
        stem = "m$a'ay+N"
        expected_map = [
        ("", ["ma'ay"]),
        ("-1SG.II", ["ma'ayi", "ma'ayu"]),
        ("-1PL.II", ["ma'aym"]),
        ("-2SG.II", ["ma'ayn"]),
        ("-2PL.II", ["ma'aysm"]),
        ("-3.II", ["ma'ayt"]),
        ("[-3.II]=CN", ["ma'ayi"]), 
        ("[-3.II]=CN.IRR", ["ma'aył"]), 
        ("[-3.II]=PN", ["ma'ays"]),
        # ("-SX", ["ma'ayit"]),
        ("-ATTR", ["ma'aym"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    @unittest.skip("need to convert to new glottal variation behavior")
    def test_glottalW(self):
        stem = "kp$a'aw+N"
        expected_map = [
            ("", ["kpa'aw"]),
            ("-1SG.II", ["kpa'awi", "kpa'awu"]),
            ("-1PL.II", ["kpa'awm"]),
            ("-2SG.II", ["kpa'awn"]),
            ("-2PL.II", ["kpa'awsm"]),
            ("-3.II", ["kpa'awt"]),
            ("[-3.II]=CN", ["kpa'awi"]),
            ("[-3.II]=CN.IRR", ["kpa'awł"]),
            ("[-3.II]=PN", ["kpa'aws"]),
            ('-SX',     ["kpa'awit"]),
            ("-ATTR", ["kpa'awm"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_glottalStop(self):
        # NOTE: this glottal should not move around
        stem = "ts'$ila'a+N"
        expected_map = [
            ("", ["ts'ila'a"]),
            ("-1SG.II", ["ts'ila'ayi", "ts'ila'ayu"]),
            ("-1PL.II", ["ts'ila'am"]),
            ("-2SG.II", ["ts'ila'an"]),
            ("-2PL.II", ["ts'ila'asm"]),
            ("-3.II", ["ts'ila'at"]),
            ("[-3.II]=CN", ["ts'ila'ayi"]),
            ("[-3.II]=CN.IRR", ["ts'ila'ał"]),
            ("[-3.II]=PN", ["ts'ila'as"]),
            # ("-SX", ["ts'ila'at"]),
            ("-ATTR", ["ts'ila'am"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_glottalStopMacron(self):
        # NOTE: this glottal should not move around
        stem = "ts'$ila_'a_+N"
        expected_map = [
            ("", ["ts'ila̱'a̱"]),
            ("-1SG.II", ["ts'ila̱'a̱yi", "ts'ila̱'a̱yu"]),
            ("-1PL.II", ["ts'ila̱'a̱m"]),
            ("-2SG.II", ["ts'ila̱'a̱n"]),
            ("-2PL.II", ["ts'ila̱'a̱sm"]),
            ("-3.II", ["ts'ila̱'a̱t"]),
            ("[-3.II]=CN", ["ts'ila̱'a̱yi"]),
            ("[-3.II]=CN.IRR", ["ts'ila̱'a̱ł"]),
            ("[-3.II]=PN", ["ts'ila̱'a̱s"]),
            # ("-SX", ["ts'ila̱'a̱t"]),
            ("-ATTR", ["ts'ila̱'a̱m"]),
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
            # ("-SX", ["wat"]),
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
            # ("-SX", ["ha'niigilbilsat"]),
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
            # ("-SX", ["gyuut"]),
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
            # ("-SX", ["yeet"]),
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
            # ("-SX", ["majag̱aleet"]),
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
            # ("-SX", ["ḵ'esiit"]),
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
            # ("-SX", ["x̱biisdit"]),
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
            # ("-SX", ["halaydit"]),
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
            # ("-SX", ["wilbit"]),
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
            # ("-SX", ["silgwit"]),
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
            # ("-SX", ["ts'amtxit"]),
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
            # ("-SX", ["biyoosxwit"]),
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
            # ("-SX", ["ax̱xwit"]),
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
            # ("-SX", ["hupx̱at"]),
            ("-ATTR", ["hupx̱am", "hupx̱a"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)


if __name__ == "__main__":
    unittest.main()

# python -m unittest test
# python -m unittest discover # all test files in current dir
# python -m unittest discover -s tests # all test files in /tests
