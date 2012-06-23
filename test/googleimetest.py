# -*- coding:utf-8 -*-

import unittest
import pyimedic
import pyimedic.googleime
import pyimedic.dctx
from StringIO import StringIO
import os

class GoogleimeTest(unittest.TestCase):
    def testReadGoogleime(self):
        msime_file = os.path.join(os.path.dirname(__file__), 'googleime2dctx.txt')
        with open(msime_file) as f:
            d = pyimedic.googleime.read(f)

        expected_file = os.path.join(os.path.dirname(__file__), 'googleime2dctx.dctx')
        with open(expected_file) as f:
            expected = f.readlines()

        f = StringIO()
        pyimedic.dctx.write(f, d)
        result = f.getvalue().split('\n')
        for e,r in zip(expected, result):
            self.assertEqual(e, r + '\n')

    def testWriteGoogleime(self):
        dctx_file = os.path.join(os.path.dirname(__file__), 'test.dctx')
        with open(dctx_file) as f:
            d = pyimedic.dctx.read(f)

        expected_file = os.path.join(os.path.dirname(__file__), 'dctx2googleime.txt')
        with open(expected_file) as f:
            expected = f.readlines()

        f = StringIO()
        pyimedic.googleime.write(f, d)
        result = f.getvalue().split('\n')
        for e,r in zip(expected, result):
            self.assertEqual(e, r + '\n')
