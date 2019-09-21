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

MY_NAME = "Abner"
print(f"|| MY name is {MY_NAME} ||")
print("="*60)

print("1. PORTAL")

print(f"GET the title and print it: {soup.title.string} ")
#print(soup.title)
#print(soup.title.string)