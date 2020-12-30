from fpdf import FPDF
from PIL import Image
import sys


def makePdf(pdfFileName, listPages, dir=''):
    if (dir):
        dir += "/"

    cover = Image.open(dir + str(listPages[0]) + ".jpg")
    width, height = cover.size

    pdf = FPDF(unit="pt", format=[width, height])

    for page in listPages:
        pdf.add_page()
        pdf.image(dir + str(page) + ".jpg", 0, 0)

    pdf.output(dir + '/converted/' + pdfFileName + ".pdf", "F")


makePdf(sys.argv[1], sys.argv[1:], 'images')
