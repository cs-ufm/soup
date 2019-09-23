#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests,sys
import csv
import json

url="http://ufm.edu/Portal"
# Make a GET request to fetch the raw HTML content
try:
    html_content = requests.get(url).text
except:
    print(f"unable to get {url}")
    sys.exit(1)

# Parse the html content, this is the Magic ;)
soup = BeautifulSoup(html_content, "html.parser")

# print if needed, gets too noisy
#print(soup.prettify())

print(soup.title)
print(soup.title.string)

#for div in soup.find_all("div"):
  #  print(div)
   # print("--------------------------")

for a in soup.find_all('a', href=True):
    print("URL encontrada:", a['href'])


    id = "menu-table"
    navBarMenu = soup.find_all("table", {"id": f"menu-table"})
    #menutable_list = []
    #print("GET all item that are part of the upper nav menu (id: menu-table)")
    for elements in navBarMenu:
        for subelement in elements.find_all("div"):
            div = subelement.string
            if div is not None:
                div = str(div).strip()
                print(f"- {div}")
                #menutable_list.append(div.strip())