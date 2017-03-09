# !/usr/bin/python
# -*- coding: utf-8 -*-

import base64
from wand.image import Image
from wand.color import Color
# http://docs.wand-py.org/en/0.4.4/index.html


def ReadPdf(inFile):
    with open(inFile) as f:
        content = base64.b64encode(f.read())
    return content

def ConvertPdf(base64_source):
    if not base64_source:
        return False

    # content = base64_source.decode('base64')
    content = base64.b64decode(base64_source)
    with Image(blob=content, resolution=150) as imgOb:
        if imgOb.width > 1400:
            ratio = 1.0 * imgOb.height/imgOb.width
            imgOb.resize(1400, int(ratio*1400))

        if imgOb.format == "PNG":
            return base64_source

        elif imgOb.format in ["JPEG", "BMP"]:
            png_bin = imgOb.make_blob("PNG")
            png_base64 = base64.b64encode(png_bin)
            return png_base64

        elif imgOb.format == "PDF":
            with imgOb.convert("PNG") as newPng:
                png_bin = newPng.make_blob()
                png_base64 = base64.b64encode(png_bin)
                return png_base64

        else:
            return base64_source

def WritePng(outFile, b64_content):
    content = base64.b64decode(b64_content)
    with open(outFile, 'w') as f:
        f.write(content)

# class ConvertToPng(object):

#     # the file inputed should be base64 encoded file object.
#     def __init__(self, inb64):
#         self.source = inb64
#         self.sourcebin = base64.b64decode(inb64)
#         self.imgOb = Image(blob=self.sourcebin, resolution=(150, 150))
#         self.format = self.imgOb.format
#         self.width = self.imgOb.width
#         self.height = self.imgOb.height

#     # return base64 encoded file object.
#     def getpng(self):
#         if self.format == "PNG":
#             return self.source
#         elif self.format in ["JPEG","BMP"]:
#             png_bin = self.imgOb.make_blob("PNG")
#             return base64.b64encode(png_bin)
#         elif self.format == "PDF":
#             with Image(width=imgOb.width, height=imgOb.height) as newImg:
#                 newImg.composite(imgOb.sequence[0], top=0, left=0)
#                 png_bin = newImg.make_blob('PNG')
#                 return png_bin


if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    WritePng('out.png', ConvertPdf(ReadPdf('b.pdf')))
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)

