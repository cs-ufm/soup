from bs4 import BeautifulSoup
import requests,sys
from inspectHtml import inspectHtml

class portal(inspectHtml):

    def getTitle(self):
        title = self.soup.title.string
        return title

    def getAddress(self):
        addres = self.soup.find("a", {"href": "#myModal"})
        return addres

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

    def run(self):
        self.parser()

        title = self.getTitle().text
        print(f"Get the title and print it: {title}")

        address = self.getAddress().text
        print(f"Get the Addres and print it: {address}")

