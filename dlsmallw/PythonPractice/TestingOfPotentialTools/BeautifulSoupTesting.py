import requests
from bs4 import BeautifulSoup
import textwrap

url = "https://edition.cnn.com/2024/10/04/politics/trump-january-6-cheney-2024-analysis/index.html"
htmlPage = requests.get(url)
soup = BeautifulSoup(htmlPage.content, "html.parser")

def addNewlineToStrings(text):
    return textwrap.wrap(text, 70, break_long_words=False)

def printAuthor():
    author = soup.find("span" ,class_="byline__name").text.strip()
    print("Author of the article: \n\t" + author)


def printPublishDate():
    publish_date = soup.find("div", class_="timestamp").text.strip()
    print("Published/Updated: \n\t" + publish_date)

def printHeadline():
    headline = soup.find(id="maincontent")
    print("Headline: \n\t" + headline.text.strip() + "\n")

def printBody():
    bodyArr = soup.find_all("p", class_="paragraph")

    i = 1
    for elem in bodyArr:
        pgText = elem.text.strip()
        lines = addNewlineToStrings(pgText)

        print(f"P{i}: \n", end="")
        for st in lines:
            print("\t" + st)

        print("\n")
        i += 1


def main():
    printHeadline()
    printBody()

main()