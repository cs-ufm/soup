#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests

url="http://ufm.edu/Portal"
# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text

# Parse the html content, this is the Magic ;)
soup = BeautifulSoup(html_content, "html.parser")

# print if needed, gets too noisy
#print(soup.prettify())

print(soup.title)
print(soup.title.string)
