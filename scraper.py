from cStringIO import StringIO
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

class Scraper(object):
    def __init__(self, pdfs, pagenums=None):
        self.pdfs = pdfs
        self.pagenums = pagenums
        self.output = None
        self.manager = None
        self.converter = None
        self.interpreter = None
        self.texts = self.scrape_all()

    def scrape_all(self):
        self.set_up()
        texts = []
        for pdf in self.pdfs:
            print pdf
            texts.append(self.scrape(pdf))
        self.clean_up()
        return texts

    def set_up(self):
        if not self.pagenums:
            self.pagenums = set()
        else:
            self.pagenums = set(self.pages)
        self.output = StringIO()
        self.manager = PDFResourceManager()
        self.converter = TextConverter(self.manager, self.output,
                                       laparams=LAParams())
        self.interpreter = PDFPageInterpreter(self.manager, self.converter)

    def scrape(self, pdf):
        infile = file(pdf, 'rb')
        print infile
        for page in PDFPage.get_pages(infile, self.pagenums):
            self.interpreter.process_page(page)
        infile.close()
        text = self.output.getvalue()
        return text
    
    def clean_up(self):
        self.converter.close()
        self.output.close()
