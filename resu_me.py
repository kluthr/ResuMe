from searcher import Searcher
from scraper import Scraper

def main():
    searcher = Searcher("AIzaSyCszAdNUh1tXp42SVANB1vxcOecmjN5kIo",
                      "007023224152901261631:ysdy_oveuxy",
                      "junior+software+engineer+resume+example+PDF")
    scraper = Scraper(searcher.pdfs)
    print scraper.texts
# Use something (PyPDF2??) to scrape the resumes
# add data to db?
# use nlg to create a new resume
# swap out keywords for other keywords

if __name__=="__main__":
    main()
