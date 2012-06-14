# -*- coding:utf-8 -*-

import unittest
import pyimedic
import pyimedic.dctx
from StringIO import StringIO

class DctxTest(unittest.TestCase):
    def testParseDctx(self):
        f = StringIO("""<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<ns1:Dictionary xmlns:ns1="http://www.microsoft.com/ime/dctx"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <ns1:DictionaryHeader>
    <ns1:DictionaryGUID>{6136b8e0-e6db-4285-86e1-98aa4653ba2b}</ns1:DictionaryGUID>
    <ns1:DictionaryLanguage>ja-jp</ns1:DictionaryLanguage>
    <ns1:DictionaryVersion>1</ns1:DictionaryVersion>
    <ns1:SourceURL>http://office.microsoft.com/ja-jp/ime/</ns1:SourceURL>
    <ns1:CommentInsertion>true</ns1:CommentInsertion>
    <ns1:DictionaryInfo Language="ja-jp">
      <ns1:ShortName>植物辞書</ns1:ShortName>
      <ns1:LongName>日本の植物名辞書</ns1:LongName>
      <ns1:Description>日本に分布する植物を収録した辞書です</ns1:Description>
      <ns1:Copyright>© 2010 Japanese Plant K.K.</ns1:Copyright>
      <ns1:CommentHeader1>分類</ns1:CommentHeader1>
      <ns1:CommentHeader2>分布地域</ns1:CommentHeader2>
      <ns1:CommentHeader3>学名</ns1:CommentHeader3>
    </ns1:DictionaryInfo>
    <ns1:DictionaryInfo Language="en-us">
      <ns1:ShortName>Plant Dictionary</ns1:ShortName>
      <ns1:LongName>Japanese Plant Dictionary</ns1:LongName>
      <ns1:Description>This dictionary contains plant names, which live in Japan.</ns1:Description>
      <ns1:Copyright>© 2010 Japanese Plant K.K.</ns1:Copyright>
      <ns1:CommentHeader1>Category</ns1:CommentHeader1>
      <ns1:CommentHeader2>Distribution</ns1:CommentHeader2>
      <ns1:CommentHeader3>Nomenclature</ns1:CommentHeader3>
    </ns1:DictionaryInfo>
  </ns1:DictionaryHeader>
  <ns1:DictionaryEntry>
    <ns1:InputString>ばっこやなぎ</ns1:InputString>
    <ns1:OutputString>婆っこ柳</ns1:OutputString>
    <ns1:PartOfSpeech>Noun</ns1:PartOfSpeech>
    <ns1:CommentData1>ヤナギ科ヤナギ属落葉高木</ns1:CommentData1>
    <ns1:CommentData2>近畿地方以北</ns1:CommentData2>
    <ns1:CommentData3>Salix Bakko</ns1:CommentData3>
    <ns1:URL>http://www.bing.com/search?q=%E5%A9%86%E3%81%A3%E3%81%93%E6%9F%B3&amp;src=IE-SearchBox&amp;FORM=IE8SRC</ns1:URL>
    <ns1:Priority>100</ns1:Priority>
    <ns1:ReverseConversion>true</ns1:ReverseConversion>
    <ns1:CommonWord>false</ns1:CommonWord>
  </ns1:DictionaryEntry>
  <ns1:DictionaryEntry>
    <ns1:InputString>ひめもち</ns1:InputString>
    <ns1:OutputString>姫黐</ns1:OutputString>
    <ns1:PartOfSpeech>Noun</ns1:PartOfSpeech>
    <ns1:CommentData1>モチノキ科モチノキ属常緑低木</ns1:CommentData1>
    <ns1:CommentData2>本州日本海側</ns1:CommentData2>
    <ns1:CommentData3>Ilex leucoclada</ns1:CommentData3>
    <ns1:URL>http://www.bing.com/search?q=%E5%A7%AB%E9%BB%90&amp;src=IE-SearchBox&amp;FORM=IE8SRC</ns1:URL>
    <ns1:Priority>100</ns1:Priority>
    <ns1:ReverseConversion>true</ns1:ReverseConversion>
    <ns1:CommonWord>false</ns1:CommonWord>
  </ns1:DictionaryEntry>
</ns1:Dictionary>
""")
        d = pyimedic.dctx.parse(f)
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
