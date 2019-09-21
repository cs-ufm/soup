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

def get_title():
    return print(f"GET the title and print it: {soup.title.string} ")

def get_address():
    return print("dir")

def get_phone():
    return print("phone")

def get_email():
    return print("email")

def get_nav_menu():
    return print("nav")

def find_href():
    return print("href")

def get_href_UFMbutton():
    return print("UFMbutton")

def get_href_MIU():
    return ("MiU")

def get_href_img():
    return ("img")

def count_a():
    return ("a")

MY_NAME = "Abner"
print("="*60)
print(f"\t\t|| MY name is {MY_NAME} ||")
print("="*60)

print("1. PORTAL")
get_title()
print("-"*60)

print(f"")