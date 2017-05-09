#!/usr/bin/python
# -*- coding: utf-8 -*-


import os
import sys


filename = sys.argv[1]
youget = "you-get '{}'\n"

with open(filename, 'r+') as f:
    print "Reading lines from file..."
    content = [youget.format(i.strip().split('&')[0]) for i in f.readlines()]
    f.seek(0)
    print "Rewriting lines to file..."
    f.writelines(content)
