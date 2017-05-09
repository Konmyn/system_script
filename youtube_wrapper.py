#!/usr/bin/python
# -*- coding: utf-8 -*-


import os
import sys


filename = sys.argv[1]
youget = "you-get '{}'\n"

file = open(filename, 'r')
content = [i.strip() for i in file.readlines()]
content = [youget.format(i) for i in content]
file.close()

file = open(filename, 'w')
file.writelines(content)
file.close()
