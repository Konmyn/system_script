from wand.image import Image


def convert_pdf_png(pdffile, outfile, pages=1):
    with Image(filename=pdffile) as pdf:
        output_page_n = min(pages, len(pdf.sequence))
        with Image(width=pdf.width, height=pdf.height*output_page_n) as img:
            page_range = xrange(output_page_n)
            for page in page_range:
                img.composite(pdf.sequence[page], top=pdf.height*page, left=0)
            img.save(filename=outfile)

convert_pdf_png('S.pdf', 'concated_img.png', 10)
