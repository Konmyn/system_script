# !/usr/bin/python
# -*- coding: utf-8 -*-

import PythonMagick
import PyPDF2
import base64
import sys
from io import BytesIO

def ReadPdf(document):
    with open(document) as f:
        content = base64.b64encode(f.read())
    return content

def PdfSniff(content):
    Image = PythonMagick.Image()
    datas = PythonMagick.Blob(content)
    Image.read(datas)
    return Image.magick()

def PdfToPng(base64_source):
    if not base64_source:
        return False

    converted = base64.b64decode(base64_source)

    if PdfSniff(converted) == "PDF":
        caches = BytesIO('wb')
        caches.write(converted)
        pypdf = PyPDF2.PdfFileReader(caches)

        for page in range(pypdf.getNumPages()):
            page_content = pypdf.getPage(page)
            write_cache = PyPDF2.PdfFileWriter()
            write_cache.addPage(page_content)

            mem_cache = BytesIO('wb')
            write_cache.write(mem_cache)
            mem_cache.seek(0)
            pdf_content = mem_cache.read()
            mem_cache.close()

            Image = PythonMagick.Image()
            Image.density("150")
            Image.read(PythonMagick.Blob(pdf_content))
            Image.magick('PNG')
            Image.write('new_0{}.png'.format(page))

        caches.close()

def main():
    cmd = sys.argv
    file_name = cmd[1]
    PdfToPng(ReadPdf(file_name))

if __name__ == "__main__":
    from timeit import default_timer
    start_time = default_timer()
    main()
    end_time = default_timer()
    print "Time used(s): {}".format(end_time - start_time)
