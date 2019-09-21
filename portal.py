from bs4 import BeautifulSoup
import requests,sys
from inspectHtml import inspectHtml

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

    def getTitle(self):
        self.title == inspectHtml.soup.title.string

    def getAddress(self):
        return print("dir")

    def getPhone(self):
        return print("phone")

    def getEmail(self):
        return print("email")

    def getNavMenu(self):
        return print("nav")

    def findHref(self):
        return print("href")

    def getHrefUFMbutton(self):
        return print("UFMbutton")

    def getHrefMIU(self):
        return ("MiU")

    def getHrefImg(self):
        return ("img")

    def countA(self):
        return ("a")

    MY_NAME = "Abner"
    print("="*60)
    print(f"\t\t|| MY name is {MY_NAME} ||")
    print("="*60)

    print("1. PORTAL")
    getTitle()
    print("-"*60)

    print(f"")