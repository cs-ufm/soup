#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests,sys
import csv
import json

class urls:
    def part1(self):
        self.url = "http://ufm.edu/Portal"

class parser:

    def parser(self):
        # Make a GET request to fetch the raw HTML content
        try:
            self.html_content = requests.get(urls.url).text
        except:
            print(f"unable to get {urls.url}")
            sys.exit(1)

        # Parse the html content, this is the Magic ;)
        self.soup = BeautifulSoup(self.html_content, "html.parser")

class portal:
    def title(self):
        print(parser.soup.title)
        print(parser.soup.title.string)

class soup:
    def start(self):
        self.parser.parser()




# url="http://ufm.edu/Portal"


# print if needed, gets too noisy
#print(soup.prettify())

#print(soup.title)
#print(soup.title.string)

#for div in soup.find_all("div"):
 #   print(div)
  #  print("--------------------------")