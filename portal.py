from bs4 import BeautifulSoup
import requests,sys

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

    def get_title(self):
        self.title == portal.soup.title.string
        return print(f"GET the title and print it: {self.title} ")

    def get_address(self):
        return print("dir")

    def get_phone(self):
        return print("phone")

    def get_email(self):
        return print("email")

    def get_nav_menu(self):
        return print("nav")

    def find_href(self):
        return print("href")

    def get_href_UFMbutton(self):
        return print("UFMbutton")

    def get_href_MIU(self):
        return ("MiU")

    def get_href_img(self):
        return ("img")

    def count_a(self):
        return ("a")

    MY_NAME = "Abner"
    print("="*60)
    print(f"\t\t|| MY name is {MY_NAME} ||")
    print("="*60)

    print("1. PORTAL")
    get_title(title)
    print("-"*60)

    print(f"")