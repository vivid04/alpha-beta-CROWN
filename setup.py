# -*- coding: utf-8 -*-
"""
Created on Wed Apr 19 12:03:14 2023

@author: hsc
"""

from distutils.core import setup, Extension

def main():
    setup(name="spam",
          version="1.0.0",
          description="Python interface for the fputs C library function",
          author="cxa",
          author_email="1598828268@qq.com",
          ext_modules=[Extension("spam", [r"D:\wordspace\cpp\spam\spammodule\spammodule\spammodule.c"])])

if __name__ == "__main__":
    main()