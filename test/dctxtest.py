# -*- coding:utf-8 -*-

import os
import unittest
import pyimedic
import pyimedic.dctx
from StringIO import StringIO

class DctxTest(unittest.TestCase):
    def testReadDctx(self):
        dctx_file = os.path.join(os.path.dirname(__file__), 'sample.dctx')
        with open(dctx_file) as f:
            d = pyimedic.dctx.read(f)

        self.assertEquals(d.GUID, "{6136b8e0-e6db-4285-86e1-98aa4653ba2b}")
        self.assertEquals(d.Language, "ja-jp")
        self.assertEquals(d.Version, 1)
        self.assertEquals(d.SourceURL, "http://office.microsoft.com/ja-jp/ime/")
        self.assertEquals(d.CommentInsertion, True)

        info_ja = d.Info['ja-jp']
        self.assertEquals(info_ja.ShortName, u'植物辞書')
        self.assertEquals(info_ja.LongName, u'日本の植物名辞書')
        self.assertEquals(info_ja.Description, u'日本に分布する植物を収録した辞書です')
        self.assertEquals(info_ja.Copyright, u'© 2010 Japanese Plant K.K.')
        self.assertEquals(info_ja.CommentHeader1, u'分類')
        self.assertEquals(info_ja.CommentHeader2, u'分布地域')
        self.assertEquals(info_ja.CommentHeader3, u'学名')

        info_en = d.Info['en-us']
        self.assertEquals(info_en.ShortName, u'Plant Dictionary')
        self.assertEquals(info_en.LongName, u'Japanese Plant Dictionary')
        self.assertEquals(info_en.Description, u'This dictionary contains plant names, which live in Japan.')
        self.assertEquals(info_en.Copyright, u'© 2010 Japanese Plant K.K.')
        self.assertEquals(info_en.CommentHeader1, u'Category')
        self.assertEquals(info_en.CommentHeader2, u'Distribution')
        self.assertEquals(info_en.CommentHeader3, u'Nomenclature')

        self.assertEquals(len(d), 2)
        self.assertEquals(d[0], pyimedic.DictionaryEntry(
                InputString = u'ばっこやなぎ',
                OutputString = u'婆っこ柳',
                PartOfSpeech = u'Noun',
                CommentData1 = u'ヤナギ科ヤナギ属落葉高木',
                CommentData2 = u'近畿地方以北',
                CommentData3 = u'Salix Bakko',
                URL = u'http://www.bing.com/search?q=%E5%A9%86%E3%81%A3%E3%81%93%E6%9F%B3&src=IE-SearchBox&FORM=IE8SRC',
                Priority = 100,
                ReverseConversion = True,
                CommonWord = False))
        self.assertEquals(d[1], pyimedic.DictionaryEntry(
                InputString = u'ひめもち',
                OutputString = u'姫黐',
                PartOfSpeech = u'Noun',
                CommentData1 = u'モチノキ科モチノキ属常緑低木',
                CommentData2 = u'本州日本海側',
                CommentData3 = u'Ilex leucoclada',
                URL = u'http://www.bing.com/search?q=%E5%A7%AB%E9%BB%90&src=IE-SearchBox&FORM=IE8SRC',
                Priority = 100,
                ReverseConversion = True,
                CommonWord = False))

    def testWriteDctx(self):
        dctx_file = os.path.join(os.path.dirname(__file__), 'sample.dctx')
        with open(dctx_file) as f:
            sample = f.read()

        d = pyimedic.dctx.read(StringIO(sample))

        f = StringIO()
        pyimedic.dctx.write(f, d)
        for a, b in zip(f.getvalue().split('\n'), sample.split('\n')):
            self.assertEqual(a, b)
