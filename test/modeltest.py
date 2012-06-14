# -*- coding:utf-8 -*-

import unittest
import pyimedic

class ModelTest(unittest.TestCase):
    def testDictionaryEntry(self):
        entry = pyimedic.makeDictionaryEntry('input', 'output')
        suppose = pyimedic.DictionaryEntry(
            InputString = 'input',
            OutputString = 'output',
            PartOfSpeech = "",
            CommentData1 = "",
            CommentData2 = "",
            CommentData3 = "",
            URL = "",
            Priority = 100,
            ReverseConversion = False,
            CommonWord = False)
        self.assertEqual(entry, suppose)

        entry = pyimedic.makeDictionaryEntry(
            'input',
            'output',
            'partofspeech',
            'comment1',
            'comment2',
            'comment3',
            'http://example.com/',
            200,
            True,
            True)
        suppose = pyimedic.DictionaryEntry(
            InputString = 'input',
            OutputString = 'output',
            PartOfSpeech = "partofspeech",
            CommentData1 = "comment1",
            CommentData2 = "comment2",
            CommentData3 = "comment3",
            URL = "http://example.com/",
            Priority = 200,
            ReverseConversion = True,
            CommonWord = True)
        self.assertEqual(entry, suppose)

    def testDictionaryEntryArgError(self):
        self.assertRaises(
            TypeError,
            pyimedic.makeDictionaryEntry)

        self.assertRaises(
            TypeError,
            pyimedic.makeDictionaryEntry,
            'input')

    def testDictionaryEntryValueError(self):
        self.assertRaises(
            ValueError,
            pyimedic.makeDictionaryEntry,
            'input',
            'output',
            URL = 'invalid URL')

        self.assertRaises(
            ValueError,
            pyimedic.makeDictionaryEntry,
            'input',
            'output',
            Priority = 256)

    def testDictioanryDefault(self):
        d = pyimedic.Dictionary()
        self.assertEqual(d.GUID, None)
        self.assertEqual(d.Language, "ja-jp")
        self.assertEqual(d.Version, 0)
        self.assertEqual(d.Version, 0)
        self.assertEqual(d.SourceURL, "")
        self.assertEqual(d.CommentInsertion, False)
        self.assertEqual(len(d.Info), 0)

    def testDictioanryGUID(self):
        def GUID(guid):
            d = pyimedic.Dictionary()
            d.GUID = guid
            self.assertEqual(d.GUID, guid)

        GUID("{03689Adf-09aF-09Af-09AF-024689AbCdEf}")
        self.assertRaises(
            ValueError,
            GUID, "03689Adf-09aF-09Af-09AF-024689AbCdEf")
        self.assertRaises(
            ValueError,
            GUID, "{03689Ad-09aF-09Af-09AF-024689AbCdEf}")
        self.assertRaises(
            ValueError,
            GUID, "{g3689Adf-09aF-09Af-09AF-024689AbCdEf}")
        self.assertRaises(
            ValueError,
            GUID, "{a03689Adf-09aF-09Af-09AF-024689AbCdEf}")

    def testDictionaryInfoDefault(self):
        info = pyimedic.DictionaryInfo()
        self.assertEqual(info.Language, "ja-jp")
        self.assertEqual(info.ShortName, "")
        self.assertEqual(info.LongName, "")
        self.assertEqual(info.Description, "")
        self.assertEqual(info.Copyright, "")
        self.assertEqual(info.CommentHeader1, "")
        self.assertEqual(info.CommentHeader2, "")
        self.assertEqual(info.CommentHeader3, "")

    def testDictionaryInfo(self):
        def Language(lang):
            info = pyimedic.DictionaryInfo()
            info.Language = lang
            self.assertEqual(info.Language, lang)
        Language('en-us')
        Language('ja-jp')
        Language('zh-cn')
        self.assertRaises(
            ValueError,
            Language, 'xx-xx')

    def testDictionaryInfoSet(self):
        d = pyimedic.Dictionary()
        info_en = pyimedic.DictionaryInfo('en-us')
        info_ja = pyimedic.DictionaryInfo('ja-jp')

        d.Info.add(info_en)
        self.assertEqual(len(d.Info), 1)
        self.assertEqual(d.Info.keys(), ['en-us'])
        self.assertEqual(d.Info.values(), [info_en])
        self.assertEqual(d.Info.items(), [['en-us', info_en]])
        self.assertEqual(d.Info['en-us'], info_en)
        self.assertRaises(IndexError, lambda: d.Info['ja-jp'])
        self.assertRaises(IndexError, lambda: d.Info['zh-cn'])

        d.Info.add(info_ja)
        self.assertEqual(len(d.Info), 2)
        self.assertEqual(d.Info.keys(), ['en-us', 'ja-jp'])
        self.assertEqual(d.Info.values(), [info_en, info_ja])
        self.assertEqual(d.Info.items(), [['en-us', info_en], ['ja-jp', info_ja]])
        self.assertEqual(d.Info['en-us'], info_en)
        self.assertEqual(d.Info['ja-jp'], info_ja)
        self.assertRaises(IndexError, lambda: d.Info['zh-cn'])

        info_ja.Language = 'zh-cn'
        self.assertEqual(len(d.Info), 2)
        self.assertEqual(d.Info.keys(), ['en-us', 'zh-cn'])
        self.assertEqual(d.Info.values(), [info_en, info_ja])
        self.assertEqual(d.Info.items(), [['en-us', info_en], ['zh-cn', info_ja]])
        self.assertEqual(d.Info['en-us'], info_en)
        self.assertRaises(IndexError, lambda: d.Info['ja-jp'])
        self.assertEqual(d.Info['zh-cn'], info_ja)

        del d.Info['en-us']
        self.assertEqual(len(d.Info), 1)
        self.assertEqual(d.Info.keys(), ['zh-cn'])
        self.assertEqual(d.Info.values(), [info_ja])
        self.assertEqual(d.Info.items(), [['zh-cn', info_ja]])
        self.assertRaises(IndexError, lambda: d.Info['en-us'])
        self.assertRaises(IndexError, lambda: d.Info['ja-jp'])
        self.assertEqual(d.Info['zh-cn'], info_ja)
