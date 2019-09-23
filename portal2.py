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

    def title(self):
        self.titles= portal.soup.title.string
        return print("GET the title and print it: <" + self.titles+">")


portalazo = portal()

print("1. Portal")
print(" ")
portalazo.title()
print("---------------------------------------")
