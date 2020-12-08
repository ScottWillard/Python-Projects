import requests
from bs4 import BeautifulSoup
import textwrap


def scrape():
    # the target we want to open

    # Example page to scrape
    url = 'https://en.wikipedia.org/wiki/Billion_laughs_attack'

    # open with GET method
    resp = requests.get(url)

    # http_respone 200 means OK status
    if resp.status_code == 200:
        print("Successfully opened the web page")

        # we need a parser,Python built-in HTML parser is enough .
        soup = BeautifulSoup(resp.text, 'html.parser')

        # l is the list which contains all the text i.e news
        reader = soup.find("div", {"class": "mw-parser-output"})

        # now we want to print only the text part of the anchor.
        # find all the elements of b, i.e anchor
        for i in reader.findAll("p"):
            print(textwrap.fill(i.text), 100)
    else:
        print("Error")


scrape()
