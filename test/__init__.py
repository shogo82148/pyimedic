#!/usr/bin/env python

import unittest
from modeltest import ModelTest
from dctxtest import DctxTest

def suite():
    s = unittest.TestSuite()
    s.addTests(unittest.makeSuite(ModelTest))
    s.addTests(unittest.makeSuite(DctxTest))
    return s

def main():
    unittest.TextTestRunner(verbosity=2).run(suite())

if __name__=="__main__":
    main()
