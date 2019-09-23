#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests,sys, csv, json, time
import os

class portal:
    url="http://ufm.edu/Portal"
    # Make a GET request to fetch the raw HTML content
    try:
        html_content = requests.get(url).text
    except:
        print(f"unable to get {url}")
        sys.exit(1)

    # Parse the html content, this is the Magic ;)
    soup = BeautifulSoup(html_content, "html.parser")

    def getCheckIfThirty(self, lines):
        return (len(lines.split('\n')) > 30)

    def checkIfThirty(self, lines):
        if self.getCheckIfThirty(lines):
            self.logError(lines)
            return print(f"Output exceeds 30 lines, logging into..")
        else:
            return print(f"{lines}")

    def title(self):
        self.titles = self.getCheckIfThirty(portal.soup.title.string)
        #self.titles = portal.soup.title.string
        return print(f"GET the title and print it: <{self.titles}>")


portalazo = portal()

print("1. Portal")
print(" ")
portalazo.title()
print("---------------------------------------")
