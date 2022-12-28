#! python
from ParseContent import Parser
from googlesearch import search
from urllib import request

class Webscraper(Parser):
    def __init__(self,urls=None,topic="",articles=10 ):
        self.urls = urls
        self.topic = topic+" news"
        self.results = []

    def scrape(self):
        """Main functionality for webscrapper."""
        count = 0

        # get urls
        if (self.urls==None):
            self.urls = self.google()
        
        # send get request
        for url in self.urls:
            with request.urlopen(url) as page:
                with open(f"pages/page{count}.html","wb") as file:
                    file.write(page.read())
                count+=1

    def google(self):
        """Scrape top 10 websites from google if url not provided."""
        return search(self.topic,num_results=10)

        

if __name__=="__main__":
    scraper = Webscraper()
    scraper.scrape()