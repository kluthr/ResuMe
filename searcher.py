from googleapiclient.discovery import build
from urllib import urlretrieve

class Searcher(object):
    def __init__(self, api_key, cse_id, terms):
        self.api_key = api_key #"AIzaSyCszAdNUh1tXp42SVANB1vxcOecmjN5kIo"
        self.cse_id = cse_id   #"007023224152901261631:ysdy_oveuxy"
        self.terms = terms     #'junior+software+engineer+resume+example+PDF'
        self.results = self.google_it(num=10)
        self.links = self.grab_links()
        self.pdfs = self.download_pdfs()

    def google_it(self, **kwargs):
         service = build("customsearch", "v1", developerKey=self.api_key)
         results = service.cse().list(q=self.terms,
                                      cx=self.cse_id, **kwargs).execute()
         return results['items']

    def grab_links(self):
        links = []
        for result in self.results:
            if result["link"][-3:] == 'pdf':
                links.append(result["link"])
        return links

    def download_pdfs(self):
        offset = 0
        pdfs = []
        for link in self.links:
            print link
            name = "example" + str(offset) +".pdf" 
            try:
                urlretrieve(link, name)
                offset += 1
                pdfs.append(name)
            except IOError:
                print "IOError!"
        print pdfs
        return pdfs
