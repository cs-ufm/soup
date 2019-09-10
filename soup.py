#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests,sys,csv,json

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

for div in soup.find_all("div"):
    print(div)
    print("--------------------------")