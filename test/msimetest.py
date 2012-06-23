# -*- coding:utf-8 -*-

import unittest
import pyimedic
import pyimedic.msime
import pyimedic.dctx
from StringIO import StringIO
import os

class MsimeTest(unittest.TestCase):
    msime_pos = [
        u'名詞',
        u'さ変名詞',
        u'ざ変名詞',
        u'形動名詞',
        u'副詞的名詞',
        u'さ変形動名詞',
        u'人名',
        u'姓',
        u'名',
        u'地名その他',
        u'固有名詞',
        u'あわ行五段',
        u'か行五段',
        u'が行五段',
        u'さ行五段',
        u'た行五段',
        u'な行五段',
        u'ば行五段',
        u'ま行五段',
        u'ら行五段',
        u'あわ行五段',
        u'か行五段',
        u'ら行五段',
        u'一段動詞',
        u'形容詞',
        u'形容動詞',
        u'副詞',
        u'連帯詞',
        u'感動詞',
        u'接頭語',
        u'姓名接頭語',
        u'地名接頭語',
        u'接尾語',
        u'姓名接尾語',
        u'助数詞',
        u'地名接尾語',
        u'慣用句',
        u'短縮よみ',
        u'顔文字',
        ]

    def testReadMsime(self):
        msime_file = os.path.join(os.path.dirname(__file__), 'msime2dctx.txt')
        with open(msime_file) as f:
            d = pyimedic.msime.read(f)

        expected_file = os.path.join(os.path.dirname(__file__), 'msime2dctx.dctx')
        with open(expected_file) as f:
            expected = f.readlines()

        f = StringIO()
        pyimedic.dctx.write(f, d)
        result = f.getvalue().split('\n')
        for e,r in zip(expected, result):
            self.assertEqual(e, r + '\n')

    def testWriteMsime(self):
        dctx_file = os.path.join(os.path.dirname(__file__), 'test.dctx')
        with open(dctx_file) as f:
            d = pyimedic.dctx.read(f)

        expected_file = os.path.join(os.path.dirname(__file__), 'dctx2msime.txt')
        with open(expected_file) as f:
            expected = f.readlines()

        f = StringIO()
        pyimedic.msime.write(f, d)
        result = f.getvalue().split('\n')
        for e,r in zip(expected, result):
            self.assertEqual(e, r + '\n')
