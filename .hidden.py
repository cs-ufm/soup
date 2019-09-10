#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests,sys

url="http://ufm.edu/Portal"
# Make a GET request to fetch the raw HTML content
try:
    html_content = requests.get(url).text
except:
    print(f"unable to get {url}")
    sys.exit(1)

# Parse the html content, this is the Magic ;)
soup = BeautifulSoup(html_content, "html.parser")

soup.find
id="menu-table"
nav_bar = soup.find_all("table", {"id":f"{id}"})

menutable_list=[]
for i in nav_bar:
    for j in i.find_all("div"):
        div=j.string
        if div is not None:
            div=str(div).strip()
            print(div)
            menutable_list.append(div.strip())

json_menutable={f"{id}": menutable_list}
print(json_menutable)