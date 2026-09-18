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
                "nab$iip",
                "g_$oot",
                "g_$amaats",
                "łg$aawk",
                "'l$ak_",
                "w$a_t'ukw",
                "w$aky", #man's brother
            ]
        }
        super().setUpClass(FULL_SGX, test_stems)

    def test_plainP(self):
        stem = "nab$iip+N"
        expected_map = [
            ("", ["nabiip"]),
            ("-1SG.II", ["nabiibi", "nabiibu"]),
            ("-1PL.II", ["nabiibm"]),
            ("-2SG.II", ["nabiibn"]),
            ("-2PL.II", ["nabiipsm"]),
            ("-3.II", ["nabiipt"]),
            ("[-3.II]=CN.IRR", ["nabiipł"]),
            ("[-3.II]=CN", ["nabiibi"]),
            ("[-3.II]=PN", ["nabiips"]),
            # ("-SX", ["nabiibit"]),
            ("-ATTR", ["nabiibm"]),
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
        stem = "g_$amaats+N"
        expected_map = [
            ("", ["g̱amaats"]),
            ("-1SG.II", ["g̱amaadzi", "g̱amaadzu"]),
            ("-1PL.II", ["g̱amaadzm"]),
            ("-2SG.II", ["g̱amaadzn"]),
            ("-2PL.II", ["g̱amaadzism"]),
            ("-3.II", ["g̱amaatst"]),
            ("[-3.II]=CN.IRR", ["g̱amaatsł"]),
            ("[-3.II]=CN", ["g̱amaadzi"]),
            ("[-3.II]=PN", ["g̱amaats"]),
            # ("-SX", ["g̱amaadzit"]),
            ("-ATTR", ["g̱amaadzm"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_plainK(self):
        stem = "łg$aawk+N"
        expected_map = [
            ("", ["łgaawk"]),
            ("-1SG.II", ["łgaawgi", "łgaawgu"]),
            ("-1PL.II", ["łgaawgm"]),
            ("-2SG.II", ["łgaawgn"]),
            ("-2PL.II", ["łgaawksm"]),
            ("-3.II", ["łgaawkt"]),
            ("[-3.II]=CN.IRR", ["łgaawkł"]),
            ("[-3.II]=CN", ["łgaawgi"]),
            ("[-3.II]=PN", ["łgaawks"]),
            # ("-SX", ["łgaawgit"]),
            ("-ATTR", ["łgaawgm"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_plainK_(self):
        stem = "'l$ak_+N"
        expected_map = [
            ("", ["'laḵ"]),
            ("-1SG.II", ["'lag̱ai", "'lag̱u"]),
            ("-1PL.II", ["'lag̱m"]),
            ("-2SG.II", ["'lag̱n"]),
            ("-2PL.II", ["'laḵsm", "'lax̱sm"]),
            ("-3.II", ["'laḵt"]),
            ("[-3.II]=CN", ["'lag̱ai"]),
            ("[-3.II]=CN.IRR", ["'laḵł", "'lax̱ł"]),
            ("[-3.II]=PN", ["'laḵs", "'lax̱s"]),
            # ("-SX", ["'lag̱it"]),
            ("-ATTR", ["'lag̱m"]),
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

    def test_plainKY(self):
        stem = "w$aky+N"
        expected_map = [
            ("", ["waky"]),
            ("-1SG.II", ["wakyi", "wakyu"]),
            ("-1PL.II", ["wakym"]),
            ("-2SG.II", ["wakyn"]),
            ("-2PL.II", ["wakysm"]),
            ("-3.II", ["wakyt"]),
            ("[-3.II]=CN", ["wakyi"]),
            ("[-3.II]=CN.IRR", ["wakył"]),
            ("[-3.II]=PN", ["wakys"]),
            # ("-SX", ["wakyit"]),
            ("-ATTR", ["wakym"]),
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

    def test_fricŁ(self):
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
                "buw$eel", #sand fleas
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

    def test_plainL(self):
        stem = "buw$eel+N"
        expected_map = [
            ("", ["buweel"]),
            ("-1SG.II", ["buweeli", "buweelu"]),
            ("-1PL.II", ["buweelm"]),
            ("-2SG.II", ["buweeln"]),
            ("-2PL.II", ["buweelsm"]),
            ("-3.II", ["buweelt"]),
            ("[-3.II]=CN", ["buweeli"]),
            ("[-3.II]=CN.IRR", ["buweeł"]),
            ("[-3.II]=PN", ["buweels"]),
            # ("-SX", ["buweelit"]),
            ("-ATTR", ["buweelm"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

class TestGlottalCoda(TestFSTOutput):

    @classmethod
    def setUpClass(cls):
        test_stems = {
            "Noun": [
                # no reason to test 'p
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
        
    def test_glottX_(self):
        stem = "han$a'ax_+N"
        expected_map = [
            ("", ["hana'ax̱","hana'ḵ"]),
            ("-1SG.II", ["hana'ag̱ai", "hana'ag̱u","hana'g̱ai", "hana'g̱u"]),
            ("-1PL.II", ["hana'ag̱m", "hana'g̱m"]),
            ("-2SG.II", ["hana'ag̱n", "hana'g̱n"]),
            ("-2PL.II", ["hana'ax̱sm", "hana'ḵsm"]),
            ("-3.II", ["hana'ax̱t","hana'ḵt"]),
            ("[-3.II]=CN", ["hana'ag̱ai","hana'g̱ai"]),
            ("[-3.II]=CN.IRR", ["hana'ax̱ł","hana'ḵł"]),
            ("[-3.II]=PN", ["hana'ax̱s","hana'ḵs"]),
            # ("-SX", ["hana'ag̱at", "hana'g̱at"]),
            ("-ATTR", ["hana'ag̱m", "hana'g̱m"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_glottalM(self):
        stem = "łił$a'am+N"
        expected_map = [
            ("", ["łiła'am","łiła'm"]),
            ("-1SG.II", ["łiła'amu", "łiła'ami", "łiła'mi", "łiła'mu"]),
            ('-1PL.II',    ["łiła'amim", "łiła'mim"]), 
            ("-2SG.II", ["łiła'amn", "łiła'mn"]),
            ("-2PL.II", ["łiła'amsm", "łiła'msm"]),
            ("-3.II", ["łiła'amt", "łiła'mt"]),
            ("[-3.II]=CN", ["łiła'ami", "łiła'mi"]),
            ("[-3.II]=CN.IRR", ["łiła'amł", "łiła'mł"]),
            ("[-3.II]=PN", ["łiła'ams", "łiła'ms"]),
            # ("-SX", ["łiła'amit", "łiła'mit"]),  
            ("-ATTR", ["łiła'amim", "łiła'mim"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_glottalN(self):
        stem = "m$o'on+N"
        expected_map = [
            ("", ["mo'on", "mo'n"]),
            ("-1SG.II", ["mo'onu", "mo'oni", "mo'nu", "mo'ni"]),
            ('-1PL.II',    ["mo'onm", "mo'nm"]), 
            ("-2SG.II", ["mo'on", "mo'n"]),
            ("-2PL.II", ["mo'onsm", "mo'nsm"]),
            ("-3.II", ["mo'ont", "mo'nt"]),
            ("[-3.II]=CN", ["mo'oni", "mo'ni"]),
            ("[-3.II]=CN.IRR", ["mo'onł", "mo'nł"]),
            ("[-3.II]=PN", ["mo'ons", "mo'ns"]),
            # ("-SX", ["mo'onit", "mo'nit"]),  
            ("-ATTR", ["mo'onm", "mo'nm"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_glottalL(self):
        stem = "lagy$i'il+N"
        expected_map = [
            ("", ["lagyi'il", "lagyi'l"]),
            ("-1SG.II", ["lagyi'ili", "lagyi'ilu", "lagyi'li", "lagyi'lu"]),
            ("-1PL.II", ["lagyi'ilm", "lagyi'lm"]),
            ("-2SG.II", ["lagyi'iln", "lagyi'ln"]),
            ("-2PL.II", ["lagyi'ilsm", "lagyi'lsm"]),
            ("-3.II", ["lagyi'ilt", "lagyi'lt"]),
            ("[-3.II]=CN", ["lagyi'ili", "lagyi'li"]),
            ("[-3.II]=CN.IRR", ["lagyi'ilł", "lagyi'ił", "lagyi'lł", "lagyi'ł"]),
            ("[-3.II]=PN", ["lagyi'ils", "lagyi'ls"]),
            # ("-SX", ["lagyi'ilit", "lagyi'lit"]),
            ("-ATTR", ["lagyi'ilm", "lagyi'lm"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_glottalY(self):
        stem = "m$a'ay+N"
        expected_map = [
        ("", ["ma'ay", "ma'y"]),
        ("-1SG.II", ["ma'ayi", "ma'ayu", "ma'yi", "ma'yu"]),
        ("-1PL.II", ["ma'aym", "ma'ym"]),
        ("-2SG.II", ["ma'ayn", "ma'yn"]),
        ("-2PL.II", ["ma'aysm", "ma'ysm"]),
        ("-3.II", ["ma'ayt", "ma'yt"]),
        ("[-3.II]=CN", ["ma'ayi", "ma'yi"]), 
        ("[-3.II]=CN.IRR", ["ma'aył", "ma'ył"]), 
        ("[-3.II]=PN", ["ma'ays", "ma'ys"]),
        # ("-SX", ["ma'ayit", "ma'yit"]),
        ("-ATTR", ["ma'aym", "ma'ym"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_glottalW(self):
        stem = "kp$a'aw+N"
        expected_map = [
            ("", ["kpa'aw", "kpa'w"]),
            ("-1SG.II", ["kpa'awi", "kpa'awu", "kpa'wi", "kpa'wu"]),
            ("-1PL.II", ["kpa'awm", "kpa'wm"]),
            ("-2SG.II", ["kpa'awn", "kpa'wn"]),
            ("-2PL.II", ["kpa'awsm", "kpa'wsm"]),
            ("-3.II", ["kpa'awt", "kpa'wt"]),
            ("[-3.II]=CN", ["kpa'awi", "kpa'wi"]),
            ("[-3.II]=CN.IRR", ["kpa'awł", "kpa'wł"]),
            ("[-3.II]=PN", ["kpa'aws", "kpa'ws"]),
            ('-SX', ["kpa'awit", "kpa'wit"]),
            ("-ATTR", ["kpa'awm", "kpa'wm"]),
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

class TestVowels(TestFSTOutput):

    @classmethod
    def setUpClass(cls):
        test_stems = {
            "Noun": [
                "d$aala", #money
                "w$aa", #name
                "hax_b$a_ta_", #butter knife
                "s$ah", #day
                "gyilksh$uu", #basket weaving; diagonal weaving
                "kłg$üü", #one's children
                "dah$dee", #cranberries
                "łmkd$ii", #opposite gender sibling
                "y$eni", #marten
                "ał$o'o", #cloth; sail; canvas  
                "gwas$oo", #pig
                "ił$i'i", #blood
                "m$anwo", #battle ship
                "n$oh" #mother
                "tgw$a_h" #glass 
            ],
        }
        super().setUpClass(FULL_SGX, test_stems)

    def test_shortA(self):
        stem = "d$aala+N"
        expected_map = [
            ("", ["daala"]),
            ("-1SG.II", ["daalayi", "daalayu"]),
            ("-1PL.II", ["daalam"]),
            ("-2SG.II", ["daalan"]),
            ("-2PL.II", ["daalasm"]),
            ("-3.II", ["daalat"]),
            ("[-3.II]=CN", ["daalayi"]),
            ("[-3.II]=CN.IRR", ["daalał"]),
            ("[-3.II]=PN", ["daalas"]),
            # ("-SX", ["daalat"]),
            ("-ATTR", ["daalam"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_shortAlonger(self):
        stem = "w$aa+N"
        expected_map = [
            ("", ["waa"]),
            ("-1SG.II", ["waayi", "waayu"]),
            ("-1PL.II", ["waam"]),
            ("-2SG.II", ["waan"]),
            ("-2PL.II", ["waasm"]),
            ("-3.II", ["waat"]),
            ("[-3.II]=CN", ["waayi"]),
            ("[-3.II]=CN.IRR", ["waał"]),
            ("[-3.II]=PN", ["waas"]),
            # ("-SX", ["waat"]),
            ("-ATTR", ["waam"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_underscoreA(self):
        stem = "hax_b$a_ta_+N"
        expected_map = [
            ("", ["hax̱ba̱ta̱"]),
            ("-1SG.II", ["hax̱ba̱ta̱yi", "hax̱ba̱ta̱yu"]), #?? hax̱ba̱ta̱i
            ("-1PL.II", ["hax̱ba̱ta̱m"]),
            ("-2SG.II", ["hax̱ba̱ta̱n"]),
            ("-2PL.II", ["hax̱ba̱ta̱sm"]),
            ("-3.II", ["hax̱ba̱ta̱t"]),
            ("[-3.II]=CN", ["hax̱ba̱ta̱yi"]), #?? hax̱ba̱ta̱i
            ("[-3.II]=CN.IRR", ["hax̱ba̱ta̱ł"]),
            ("[-3.II]=PN", ["hax̱ba̱ta̱s"]),
            # ("-SX", ["hax̱ba̱ta̱t"]),
            ("-ATTR", ["hax̱ba̱ta̱m"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_shortAH(self):
        stem = "s$ah+N"
        expected_map = [
            ("", ["sah"]),
            ("-1SG.II", ["sái", "sayi", "sahyu"]), # not sayu? 
            ("-1PL.II", ["sahm"]),
            ("-2SG.II", ["sahn"]),
            ("-2PL.II", ["sahsm"]),
            ("-3.II", ["sáit"]), #?? saht
            ("[-3.II]=CN", ["sái", "sayi"]), #?? same as -1SG.II
            ("[-3.II]=CN.IRR", ["sahł"]),
            ("[-3.II]=PN", ["sáit"]), #?? not saht
            # ("-SX", ["sáit"]), #?? not sahit, saht
            ("-ATTR", ["sahm"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)


    def test_longU(self):
        stem = "gyilksh$uu+N"
        expected_map = [
            ("", ["gyilkshuu"]),
            ("-1SG.II", ["gyilkshuuyi", "gyilkshuuyu"]), # ?? gyilkshuu 
            ("-1PL.II", ["gyilkshuum"]),
            ("-2SG.II", ["gyilkshuun"]),
            ("-2PL.II", ["gyilkshuusm"]),
            ("-3.II", ["gyilkshuut"]),
            ("[-3.II]=CN", ["gyilkshuuyi"]),
            ("[-3.II]=CN.IRR", ["gyilkshuuł"]),
            ("[-3.II]=PN", ["gyilkshuus"]), 
            # ("-SX", ["gyilkshuut"]),
            ("-ATTR", ["gyilkshuum"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_longUmlautU(self):
        stem = "kłg$üü+N"
        expected_map = [
            ("", ["kłgüü"]),
            ("-1SG.II", ["kłgüüyi", "kłgüüyu"]),  
            ("-1PL.II", ["kłgüüm"]),
            ("-2SG.II", ["kłgüün"]),
            ("-2PL.II", ["kłgüüsm"]),
            ("-3.II", ["kłgüüt"]),
            ("[-3.II]=CN", ["kłgüüyi"]),
            ("[-3.II]=CN.IRR", ["kłgüüł"]),
            ("[-3.II]=PN", ["kłgüüs"]), 
            # ("-SX", ["kłgüüt"]),
            ("-ATTR", ["kłgüüm"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_shortElonger(self):
        stem = "dahd$ee+N"
        expected_map = [
            ("", ["dahdee"]),
            ("-1SG.II", ["dahdeeyi", "dahdeeyu"]),  
            ("-1PL.II", ["dahdeem"]),
            ("-2SG.II", ["dahdeen"]),
            ("-2PL.II", ["dahdeesm"]),
            ("-3.II", ["dahdeet"]),
            ("[-3.II]=CN", ["dahdeeyi"]),
            ("[-3.II]=CN.IRR", ["dahdeeł"]),
            ("[-3.II]=PN", ["dahdees"]), 
            # ("-SX", ["dahdeet"]),
            ("-ATTR", ["dahdeem"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_longI(self):
        stem = "łmkd$ii+N"
        expected_map = [
            ("", ["łmkdii"]),
            ("-1SG.II", ["łmkdiiyi", "łmkdiiyu"]),  
            ("-1PL.II", ["łmkdiim"]),
            ("-2SG.II", ["łmkdiin"]),
            ("-2PL.II", ["łmkdiism"]),
            ("-3.II", ["łmkdiit"]),
            ("[-3.II]=CN", ["łmkdii"]), #no -yi
            ("[-3.II]=CN.IRR", ["łmkdiił"]),
            ("[-3.II]=PN", ["łmkdiis"]), 
            # ("-SX", ["łmkdiit"]), 
            ("-ATTR", ["łmkdiim"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_shortI(self):
        stem = "y$eni+N"
        expected_map = [
            ("", ["yeni"]),
            ("-1SG.II", ["yeniyi", "yeniyu"]),  
            ("-1PL.II", ["yenim"]),
            ("-2SG.II", ["yenin"]),
            ("-2PL.II", ["yenism"]),
            ("-3.II", ["yenit"]),
            ("[-3.II]=CN", ["yeni"]), # no -yi
            ("[-3.II]=CN.IRR", ["yenił"]),
            ("[-3.II]=PN", ["yenis"]), 
            # ("-SX", ["yenit"]),
            ("-ATTR", ["yenim"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_glottO(self):
        stem = "ał$o'o+N"
        expected_map = [
            ("", ["ało'o"]),
            ("-1SG.II", ["ało'oyi", "ało'oyu", "ałoo'yi", "ało'yi", "ałoo'yu", "ało'yu"]),  # not sure about glottal movement if any
            ("-1PL.II", ["ało'om", "ało'm"]), 
            ("-2SG.II", ["ało'on", "ało'n"]),
            ("-2PL.II", ["ało'osm", "ało'sm"]),
            ("-3.II", ["ało'ot", "ało't"]),
            ("[-3.II]=CN", ["ało'oyi", "ałoo'yi", "ało'yi"]),
            ("[-3.II]=CN.IRR", ["ało'oł", "ało'ł"]),
            ("[-3.II]=PN", ["ało'os", "ało's"]), 
            # ("-SX", ["ało'ot", "ało't"]),
            ("-ATTR", ["ało'om", "ało'm"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_longOO(self):
        stem = "gwas$OO+N"
        expected_map = [
            ("", ["gwasoo"]),
            ("-1SG.II", ["gwasooyi", "gwasooyu"]), 
            ("-1PL.II", ["gwasoom"]), 
            ("-2SG.II", ["gwasoon"]),
            ("-2PL.II", ["gwasoosm"]),
            ("-3.II", ["gwasoot"]),
            ("[-3.II]=CN", ["gwasooyi"]),
            ("[-3.II]=CN.IRR", ["gwasooł"]),
            ("[-3.II]=PN", ["gwasoos"]), 
            # ("-SX", ["gwasoot"]),
            ("-ATTR", ["gwasoom"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_longOO(self):
        stem = "ił$i'i+N"
        expected_map = [
            ("", ["iłi'i"]),
            ("-1SG.II", ["iłi'iyi", "iłi'iyu", "iłii'yi", "iłi'yi", "iłii'yu", "iłi'yu"]), # not sure about glottal movement if any
            ("-1PL.II", ["iłi'im", "iłi'm"]), 
            ("-2SG.II", ["iłi'in", "iłi'n"]),
            ("-2PL.II", ["iłi'ism", "iłi'sm"]),
            ("-3.II", ["iłi'it", "iłi't"]),
            ("[-3.II]=CN", ["iłii'i", "iłi'i"]), #no -yi like with normal short / long i
            ("[-3.II]=CN.IRR", ["iłi'ił", "iłi'ł"]),
            ("[-3.II]=PN", ["iłi'is", "iłi's"]), 
            # ("-SX", ["iłi'it", "iłi't"]),
            ("-ATTR", ["iłi'im", "iłi'm"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_shortO(self):
        stem = "m$anwo+N"
        expected_map = [
            ("", ["manwo"]),
            ("-1SG.II", ["manwoyi", "manwoyu"]), 
            ("-1PL.II", ["manwom"]), 
            ("-2SG.II", ["manwon"]),
            ("-2PL.II", ["manwosm"]),
            ("-3.II", ["manwot"]),
            ("[-3.II]=CN", ["manwoyi"]), 
            ("[-3.II]=CN.IRR", ["manwoł"]),
            ("[-3.II]=PN", ["manwos"]), 
            # ("-SX", ["manwot"]),
            ("-ATTR", ["manwom"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_shortOH(self):
        stem = "n$oh+N"
        expected_map = [
            ("", ["noh", "no"]),
            ("-1SG.II", ["nohoi", "nohu"]), #not sure about nohoi, maybe nói
            ("-1PL.II", ["nohom"]), #o epnethsis
            ("-2SG.II", ["nohon"]), #o epenthesis
            ("-2PL.II", ["nosm", "nohsm"]), #not sure about nohsm
            ("-3.II", ["nohot", "not"]), #not sure about no(h)t
            ("[-3.II]=CN", ["nohoi"]), #not sure about nohoi, maybe nói
            ("[-3.II]=CN.IRR", ["nohł"]),
            ("[-3.II]=PN", ["nos", "nohs"]), #not sure about nohs 
            # ("-SX", ["nohot", "not"]), #not sure about no(h)t
            ("-ATTR", ["nohom"]), #o epenthesis
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_glottA(self):
        stem = "niy$a'a+N"
        expected_map = [
            ("", ["niya'a"]),
            ("-1SG.II", ["niya'ayi", "niya'ayu", "niyaa'yi", "niyaa'yu","niy'ayi", "niy'ayu"]), #not sure about glottal movement
            ("-1PL.II", ["niy'aam", "niy'am"]), 
            ("-2SG.II", ["niy'aan", "niy'an"]), 
            ("-2PL.II", ["niy'aasm", "niy'asm"]), 
            ("-3.II", ["niy'aat", "niy'at"]), 
            ("[-3.II]=CN", ["niy'aayi", "niy'ayi"]), 
            ("[-3.II]=CN.IRR", ["niy'aał", "niy'ał"]),
            ("[-3.II]=PN", ["niy'aas", "niy'as"]), 
            # ("-SX", ["niy'aat", "niy'at"]), 
            ("-ATTR", ["niy'aam", "niy'am"]), 
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_glottA(self):
        stem = "tgw$a_h+N"
        expected_map = [
            ("", ["tgwa̱h"]),
            ("-1SG.II", ["tgwá̱i", "tgwa̱yi" "tgwa̱hyu"]), #not sure about a_ and H-deletion
            ("-1PL.II", ["tgwa̱hm"]), 
            ("-2SG.II", ["tgwa̱hn"]), 
            ("-2PL.II", ["tgwa̱hsm"]), 
            ("-3.II", ["tgwá̱it"]), #?? tgwa̱ht 
            ("[-3.II]=CN", ["tgwá̱i", "tgwa̱yi"]), #?? same -SG.II 
            ("[-3.II]=CN.IRR", ["tgwa̱hł"]),
            ("[-3.II]=PN", ["tgwa̱it"]), #?? not tgwa̱ht
            # ("-SX", ["tgwá̱it"]), #?? not tgwa̱hit, tgwa̱ht 
            ("-ATTR", ["tgwa̱hm"]), 

        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

class TestClusters(TestFSTOutput):

    @classmethod
    def setUpClass(cls):
        test_stems = {
            "Noun": [
                "h$ap'ast", #lid  
                "l$aalt", #snake
                "w$aalp", #house
                "m$atxy", #mountain goat
                "m$alk", #bark; dry skin
                "b$a_x_bog_mgyemk", #butterly
                "l$iimxy", #song
                "$iimx_", #beard
                "t'$u'utsk", #knife; iron
                "łg$uułk", #one's child
                "d$asx_", #squirrel
                "l$ax_s", #nails; claws
                "$aẅs", #sand
            ]
        }
        super().setUpClass(FULL_SGX, test_stems)

    def test_ST(self):
        stem = "h$ap'ast+N"
        expected_map = [
            ("", ["hap'ast"]),
            ("-1SG.II", ["hap'asdi", "hap'asdu"]),
            ("-1PL.II", ["hap'asdm"]),
            ("-2SG.II", ["hap'asdn"]),
            ("-2PL.II", ["hap'astsm"]),
            ("-3.II", ["hap'ast"]),
            ("[-3.II]=CN", ["hap'asdi"]),
            ("[-3.II]=CN.IRR", ["hap'astł"]),
            ("[-3.II]=PN", ["hap'asts"]),
            # ("-SX", ["hap'asdit"]),
            ("-ATTR", ["hap'asdm"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_LT(self):
        stem = "l$aalt+N"
        expected_map = [
            ("", ["laalt"]),
            ("-1SG.II", ["laaldi", "laaldu"]),
            ("-1PL.II", ["laaldm"]),
            ("-2SG.II", ["laaldn"]),
            ("-2PL.II", ["laaltsm"]),
            ("-3.II", ["laalt"]),
            ("[-3.II]=CN", ["laaldi"]),
            ("[-3.II]=CN.IRR", ["laaltł"]),
            ("[-3.II]=PN", ["laalts"]),
            # ("-SX", ["laaldit"]),
            ("-ATTR", ["laaldm"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_LP(self):
        stem = "w$aalp+N"
        expected_map = [
            ("", ["waalp"]),
            ("-1SG.II", ["waalbi", "waalbu"]),
            ("-1PL.II", ["waalbm"]),
            ("-2SG.II", ["waalbn"]),
            ("-2PL.II", ["waalpsm"]),
            ("-3.II", ["waalpt"]),
            ("[-3.II]=CN", ["waalbi"]),
            ("[-3.II]=CN.IRR", ["waalpł"]),
            ("[-3.II]=PN", ["waalps"]),
            # ("-SX", ["waalbit"]),
            ("-ATTR", ["waalbm"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_LK(self):
        stem = "m$alk+N"
        expected_map = [
            ("", ["malk"]),
            ("-1SG.II", ["malgi", "malgu"]),
            ("-1PL.II", ["malgm"]),
            ("-2SG.II", ["malgn"]),
            ("-2PL.II", ["malksm"]),
            ("-3.II", ["malkt"]),
            ("[-3.II]=CN", ["malgi"]),
            ("[-3.II]=CN.IRR", ["malkł"]),
            ("[-3.II]=PN", ["malks"]),
            # ("-SX", ["malgit"]),
            ("-ATTR", ["malgm"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_LK(self):
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

    def test_TXY(self):
        stem = "m$atxy+N"
        expected_map = [
            ("", ["matxy"]),
            ("-1SG.II", ["matxyi", "matxyu"]),
            ("-1PL.II", ["matxym"]),
            ("-2SG.II", ["matxyn"]),
            ("-2PL.II", ["matxysm"]),
            ("-3.II", ["matxyt"]),
            ("[-3.II]=CN", ["matxyi"]),
            ("[-3.II]=CN.IRR", ["matxył"]),
            ("[-3.II]=PN", ["matxys"]),
            # ("-SX", ["matxyit"]),
            ("-ATTR", ["matxym"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_MXY(self):
        stem = "l$iimxy+N"
        expected_map = [
            ("", ["liimxy"]),
            ("-1SG.II", ["liimxyi", "liimxyu"]),
            ("-1PL.II", ["liimxym"]), 
            ("-2SG.II", ["liimxyn"]),
            ("-2PL.II", ["liimxysm"]),
            ("-3.II", ["liimxyt"]),
            ("[-3.II]=CN", ["liimxyi"]),
            ("[-3.II]=CN.IRR", ["liimxył"]),
            ("[-3.II]=PN", ["liimxys"]),
            # ("-SX", ["liimxyit"]),
            ("-ATTR", ["liimxym"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_MX_(self):
        stem = "$iimx_+N"
        expected_map = [
            ("", ["iimx̱"]),
            ("-1SG.II", ["iimg̱ai", "iimg̱u"]),
            ("-1PL.II", ["iimg̱m"]), 
            ("-2SG.II", ["iimg̱n"]),
            ("-2PL.II", ["iimx̱sm"]),
            ("-3.II", ["iimx̱t"]),
            ("[-3.II]=CN", ["iimg̱ai"]),
            ("[-3.II]=CN.IRR", ["iimx̱ł"]),
            ("[-3.II]=PN", ["iimx̱s"]),
            # ("-SX", ["iimg̱it"]),
            ("-ATTR", ["iimg̱m"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_SK(self):
        stem = "t'$u'utsk+N"
        expected_map = [
            ("", ["t'u'utsk"]),
            ("-1SG.II", ["t'u'utsgi", "t'u'utsgu"]),
            ("-1PL.II", ["t'u'utsgm"]),
            ("-2SG.II", ["t'u'utsgn"]),
            ("-2PL.II", ["t'u'utsksm"]),
            ("-3.II", ["t'u'utskt"]),
            ("[-3.II]=CN", ["t'u'utsgi"]),
            ("[-3.II]=CN.IRR", ["t'u'utskł"]),
            ("[-3.II]=PN", ["t'u'utsks"]),
            # ("-SX", ["t'u'utsgit"]),
            ("-ATTR", ["t'u'utsgm"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_ŁK(self):
        stem = "łg$uułk+N"
        expected_map = [
            ("", ["łguułk"]),
            ("-1SG.II", ["łguułgi", "łguułgu"]),
            ("-1PL.II", ["łguułgm"]),
            ("-2SG.II", ["łguułgn"]),
            ("-2PL.II", ["łguułksm"]),
            ("-3.II", ["łguułkt"]),
            ("[-3.II]=CN", ["łguułgi"]),
            ("[-3.II]=CN.IRR", ["łguułkł"]),
            ("[-3.II]=PN", ["łguułks"]),
            # ("-SX", ["łguułgit"]),
            ("-ATTR", ["łguułgm"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_SX_(self):
        stem = "d$asx_+N"
        expected_map = [
            ("", ["dasx̱"]),
            ("-1SG.II", ["dasx̱ai", "dasx̱u"]),
            ("-1PL.II", ["dasx̱m"]),
            ("-2SG.II", ["dasx̱n"]),
            ("-2PL.II", ["dasx̱sm"]),
            ("-3.II", ["dasx̱t"]),
            ("[-3.II]=CN", ["dasx̱ai"]),
            ("[-3.II]=CN.IRR", ["dasx̱ł"]),
            ("[-3.II]=PN", ["dasx̱s"]),
            # ("-SX", ["dasx̱it"]),
            ("-ATTR", ["dasx̱m"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_X_S(self):
        stem = "l$ax_s+N"
        expected_map = [
            ("", ["lax̱s"]),
            ("-1SG.II", ["lax̱si", "lax̱su"]),
            ("-1PL.II", ["lax̱sm"]),
            ("-2SG.II", ["lax̱sn"]),
            ("-2PL.II", ["lax̱sm"]), #probably not lax̱sism
            ("-3.II", ["lax̱st"]),
            ("[-3.II]=CN", ["lax̱si"]),
            ("[-3.II]=CN.IRR", ["lax̱sł"]),
            ("[-3.II]=PN", ["lax̱s"]), #probably not lax̱sis, lax̱ss
            # ("-SX", ["lax̱sit"]),
            ("-ATTR", ["lax̱sm"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

    def test_WDOTS(self):
        stem = "$aẅs+N"
        expected_map = [
            ("", ["aẅs"]),
            ("-1SG.II", ["aẅsi", "aẅsu"]),
            ("-1PL.II", ["aẅsm"]),
            ("-2SG.II", ["aẅsn"]),
            ("-2PL.II", ["aẅsm"]), #probably not aẅsism
            ("-3.II", ["aẅst"]),
            ("[-3.II]=CN", ["aẅsi"]),
            ("[-3.II]=CN.IRR", ["aẅsł"]),
            ("[-3.II]=PN", ["aẅs"]), #probably not aẅsis, aẅss
            # ("-SX", ["aẅsit"]),
            ("-ATTR", ["aẅsm"]),
        ]
        self.checkManyInFST(stem_gloss=stem, expected_map=expected_map)

if __name__ == "__main__":
    unittest.main()

# python -m unittest test
# python -m unittest discover # all test files in current dir
# python -m unittest discover -s tests # all test files in /tests
