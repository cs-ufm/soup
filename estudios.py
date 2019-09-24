#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests,sys, csv, json, time
import os
import shutil

class estudios:
    url="http://ufm.edu/Estudios"
    # Make a GET request to fetch the raw HTML content
    try:
        html_content = requests.get(url).text
    except:
        print(f"unable to get {url}")
        sys.exit(1)

    # Parse the html content, this is the Magic ;)
    soup = BeautifulSoup(html_content, "html.parser")

    def logFileWriter(self, lines, nameOfFile):
        file = open(f"{nameOfFile}", "w")
        file.write(lines)
        file.close()
        shutil.move(f'{nameOfFile}', 'logs')

    def getCheckIfThirty(self, lines):
        return (len(lines.split('\n')) > 30)

    def checkIfThirty(self, lines, func):
        if self.getCheckIfThirty(lines):
            #self.logError(lines)
            self.nameOfOutputLogFile = f"2Estudios_{func}.txt"
            self.logFileWriter(lines, self.nameOfOutputLogFile)
            return f"Output exceeds 30 lines, sending output to: {self.nameOfOutputLogFile}"
        else:
            return f"{lines}"

    def getTitle(self):
        self.nameFunction = "GET_the_title_and_print_it"
        self.titles = self.checkIfThirty(estudios.soup.title.string, self.nameFunction)
        #self.titles = portal.soup.title.string
        return print(f"GET the title and print it: <{self.titles}>")

    def getUpenTopElements(self):
        self.nameFunction = "GET_all_item_that_are_part_of_the_top_menu"
        navBarMenu = self.soup.find_all("div", {"id": f"topmenu"})
        for elements in navBarMenu:
            for subelement in elements.find_all("li"):
                div = subelement.string
                if div is not None:
                    div = str(div).strip()
                    print(f"- {div}")

    def getEstudios(self):
        self.nameFunction = "display_ALL_Estudios"
        for todosEstudios in self.soup.findAll('div', {'class': 'estudios'}):
            print("- " + todosEstudios.text)

    def displayLeftbar(self):
        self.nameFunction = "display_from_leftbar_all_<li>_items"
        for itemLeft in self.soup.findAll('div', {'class': 'leftbar'}):
            for item in itemLeft.find_all('a'):
                print("- " + item.text)

    def displaySocialMedia(self):
        self.nameFunction = "get_and_display_all_available_social_media"
        for itemLeft in self.soup.findAll('div', {'class': 'social pull-right'}):
            for item in itemLeft.find_all('a'):
                print("- " + item.get('href'))

    def countAEst(self):
        self.countAllA = len(self.soup.find_all('a', href=True))
        return print(f"Count all <a>: {self.countAllA}")

print("="*60)
print("2. Estudios")
estudiazo = estudios()
print("-"*60)
estudiazo.getTitle()
print("-"*60)
estudiazo.getUpenTopElements()
print("-"*60)
estudiazo.getEstudios()
print("-"*60)
estudiazo.displayLeftbar()
print("-"*60)
estudiazo.displaySocialMedia()
print("-"*60)
estudiazo.countAEst()