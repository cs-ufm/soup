#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests,sys
import csv
import json
from portal import portal

class soup:

    def __init__(self):
        self.portal = portal("http://ufm.edu/Portal")


# url="http://ufm.edu/Portal"


# print if needed, gets too noisy
#print(soup.prettify())

#print(soup.title)
#print(soup.title.string)

#for div in soup.find_all("div"):
 #   print(div)
  #  print("--------------------------")