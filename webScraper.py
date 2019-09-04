import urllib.request
from bs4 import BeautifulSoup


class Scrapper:

    def __init__(self, site):
        self.site = site


    def scrape(self):
        r = urllib.request\
                .urlopen(self.site)
        html = r.read()
        parser = 'html.parser'
        sp = BeautifulSoup(html,parser)
        for tag in sp.find_all("a"):
            url = tag.get("href")
            if url is None:
                continue
            if "html" in url:
                print('\n' + url)

news = 'https://news.google.com'
Scrapper(news).scrape()
print('Hello')