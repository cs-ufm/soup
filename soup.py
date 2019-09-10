from bs4 import BeautifulSoup
import requests

#url="https://en.wikipedia.org/wiki/List_of_countries_by_GDP_(nominal)"
url="http://ufm.edu/Portal"
# Make a GET request to fetch the raw HTML content
html_content = requests.get(url).text

# Parse the html content
soup = BeautifulSoup(html_content, "html.parser")
#print(soup.prettify())

print(soup.title)
print(soup.title.string)
