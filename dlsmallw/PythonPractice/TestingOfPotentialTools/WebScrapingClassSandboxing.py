import requests
from bs4 import BeautifulSoup
import textwrap

# This is a sort of prototype for a potential WebScrape class.
# The general idea is that we can use a class to automatically parse data when creating the object,
# and then use that object to get specific details from the parsed data.
class ScrapedData:
    def __init__(self, url):
        self.url = url
        self.soup = None
        self.raw_html = None
        self.author = None
        self.title = None
        self.publish_date = None
        self.body = None

        self.__buildSoup()
        self.__populateFields()

    def __textFormatter(self, text):
        text_arr = textwrap.wrap(text, 70, break_long_words=False)
        joinedSt = ""

        for st in text_arr:
            joinedSt += "\t" + st + "\n"

        return joinedSt

    def __buildSoup(self):
        self.raw_html = requests.get(self.url)
        self.soup = BeautifulSoup(self.raw_html.content, "html.parser")

    def __populateFields(self):
        soup = self.soup

        self.author = soup.find("span", class_="byline__name")
        self.publish_date = soup.find("div", class_="timestamp")
        self.title = soup.find(id="maincontent")
        self.body = soup.find_all("p", class_="paragraph")

    def printUrlData(self):
        print("Title: \n" + self.__textFormatter(self.title.text.strip()))
        print("Author: \n" + self.__textFormatter(self.author.text.strip()))
        print("Published/Updated: \n" + self.__textFormatter(self.publish_date.text.strip()))

        i = 1
        for pg in self.body:
            print(f"Paragraph-{i}: \n" + self.__textFormatter(pg.text.strip()))
            i += 1

scrapedData = ScrapedData("https://edition.cnn.com/2024/10/04/politics/trump-january-6-cheney-2024-analysis/index.html")
scrapedData.printUrlData()