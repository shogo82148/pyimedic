#!/usr/bin/env python
#-*- coding:utf-8 -*-

try:
    from setuptools import setup
except:
    from distutils.core import setup

from email.Utils import parseaddr
import pyimedic

name = pyimedic.__name__
author, email = parseaddr(pyimedic.__author__)

setup(
    name = name,
    version = pyimedic.__version__,
    author = author,
    author_email = email,
    url = pyimedic.__url__,
    license = pyimedic.__license__,
    packages = ['pyimedic'],
    platforms = ["any"],
    test_suite = "test.suite"
    )
