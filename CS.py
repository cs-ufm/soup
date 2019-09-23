#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests,sys, csv, json, time
import os
import shutil
import urllib.request

class CS:
    url= "https://fce.ufm.edu/carrera/cs/"
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
            self.nameOfOutputLogFile = f"3CS_{func}.txt"
            self.logFileWriter(lines, self.nameOfOutputLogFile)
            return f"Output exceeds 30 lines, sending output to: {self.nameOfOutputLogFile}"
        else:
            return f"{lines}"

    def getTitle(self):
        self.nameFunction = "GET_the_title_and_print_it"
        self.titles = self.checkIfThirty(CS.soup.title.string, self.nameFunction)
        #self.titles = portal.soup.title.string
        return print(f"GET the title and print it: <{self.titles}>")

    def findHrefCS(self):
        self.nameFunction = "find_all_properties_that_have_href_CS"
        hrefs = ""
        for href in self.soup.find_all(href=True):
            hrefs += f" - {href}\n"
        self.myhrefs = self.checkIfThirty(hrefs, self.nameFunction)
        return print(f"GET the href and print it: {self.myhrefs}")

    def downloadLogoFCE(self):
        self.nameFunction = "download_the_FCE_logo"
        for img in self.soup.find_all('img', {'class': 'fl-photo-img wp-image-500 size-full'}):
            self.logoLink = img.get('src')
            urllib.request.urlretrieve(self.logoLink, 'FCElogo.png')
        return print("Image downloaded")

    def getMetaOg(self):
        self.nameFunction = "returns_meta_title_and_description"
        for item in self.soup.findAll('meta', {'property': 'og:title'}):
            content = item.get('content')
        for item in self.soup.findAll('meta', {'property': 'og:description'}):
            descripcion = item.get('content')
        return print(f"Título: {content}, Description:  {descripcion}")

    def countACS(self):
        self.nameFunction = "count_all_a_in_CS"
        self.countAllA = len(self.soup.find_all('a', href=True))
        return print(f"Total de <a> en CS: {self.countAllA}")

    def countDivCS(self):
        self.nameFunction = "count_all_div_in_CS"
        self.countAllDiv = len(self.soup.find_all('div'))
        return print(f"Total de <div> en CS: {self.countAllDiv}")

print("3. CS")
print("-"*60)
csazo = CS()
csazo.getTitle()
print("-"*60)
csazo.findHrefCS()
print("-"*60)
csazo.downloadLogoFCE()
print("-"*60)
csazo.getMetaOg()
print("-"*60)
csazo.countACS()
print("-"*60)
csazo.countDivCS()


