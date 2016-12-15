#!/usr/bin/python
# -*- coding: utf-8 -*-

import PyPDF2
import PythonMagick

input_pdf = file("SO028__2016-12-12.pdf", "rb")
pdf_file = PyPDF2.PdfFileReader(input_pdf)
page_count = pdf_file.getNumPages()
page_num = 0
for page_num in range(page_count):
    img_obj = PythonMagick.Image()
    img_obj.density("150")
    img_obj.read("SO028__2016-12-12.pdf[{}]".format(page_num))
    img_obj.magick('PNG')
    img_obj.write("new{}.png".format(page_num))

import PythonMagick
page_num = 0
img_obj = PythonMagick.Image()
img_obj.density("150")
while True:
    try:
        img_obj.read("SO028__2016-12-12.pdf[{}]".format(page_num))
    except:
        break
    img_obj.magick('PNG')
    img_obj.write("what{}.png".format(page_num))
    page_num += 1

# !/usr/bin/python
# -*- coding: utf-8 -*-
# te_author    : 蛙鳜鸡鹳狸猿
# create_time  : 2016年 11月 01日 星期二 17:38:06 CST
# NOTICE       : *_* script of manipulating pdf*_*


import sys
import PyPDF2
import PythonMagick


# class obj
class ManImage:
    def __init__(self, i_file, o_dire):
        self.i_file = i_file    # input  file
        self.o_dire = o_dire    # output directory

    def __str__(self):
        traceback = "Executing under {0.argv[0]} of {1.i_file} into {2.o_dire}......".format(sys, self, self)
        return traceback

    # .pdf file to .png files
    def playpdf(self, ds):    # arg__"ds" = 1024 ~= 1MB under my test
        pages = PyPDF2.PdfFileReader(file(self.i_file, "rb")).getNumPages()
        print('Totally get ***{0:^4}*** pages from "{1.i_file}", playpdf start......'.format(pages, self))
        try:
            for i in range(pages):
                image = PythonMagick.Image()
                image.density(str(ds))
                image.read(self.i_file + '[' + str(i) + ']')
                image.magick("PNG")
                image.write(self.o_dire + str(i + 1) + ".png")
                print("{0:>5}     page OK......".format(i + 1))
        except Exception, e:
            print(str(e))



# !/usr/bin/python
# -*- coding: utf-8 -*-
# te_author    : 蛙鳜鸡鹳狸猿
# create_time  : 2016年 11月 01日 星期二 17:38:06 CST
# NOTICE       : *_* script of converting .pdf to .png*_*


import sys
import class_image


i_file = sys.argv[1]
o_dire = sys.argv[2]
ds = sys.argv[3]

if i_file[-4:] == ".pdf":
    class_image.ManImage(i_file=i_file, o_dire=o_dire).playpdf(ds=ds)
else:
    exit()