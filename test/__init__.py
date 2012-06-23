#!/usr/bin/env python

import unittest
from modeltest import ModelTest
from dctxtest import DctxTest
from msimetest import MsimeTest

def suite():
    s = unittest.TestSuite()
    s.addTests(unittest.makeSuite(ModelTest))
    s.addTests(unittest.makeSuite(DctxTest))
    s.addTests(unittest.makeSuite(MsimeTest))
    return s

def main():
    unittest.TextTestRunner(verbosity=2).run(suite())

if __name__=="__main__":
    main()
