#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests,sys, csv, json, time
import os
import shutil

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
            self.nameOfOutputLogFile = f"1portal_{func}.txt"
            self.logFileWriter(lines, self.nameOfOutputLogFile)
            return f"Output exceeds 30 lines, sending output to: {self.nameOfOutputLogFile}"
        else:
            return f"{lines}"

    def getTitle(self):
        self.nameFunction = "GET_the_title_and_print_it"
        self.titles = self.checkIfThirty(portal.soup.title.string, self.nameFunction)
        #self.titles = portal.soup.title.string
        return print(f"GET the title and print it: <{self.titles}>")

    variables = soup.find_all('a', href=True)

    def getAddress(self):

        self.nameFunction = "GET_the_Complete_Address_of_UFM"
        self.address = self.checkIfThirty(self.variables[291].text, self.nameFunction)
        return print(f"GET the Complete Address of UFM: <{self.address}>")

    def getPhoneEmail(self):
        self.nameFunction = "GET_the_phone_number_and_info_email"
        self.phone = self.checkIfThirty(self.variables[292].text, self.nameFunction)
        self.email = self.checkIfThirty(self.variables[293].text, self.nameFunction)
        return print(f"GET the phone: <{self.phone}> and email <{self.email}>")

    def getUpenNavElements(self):
        self.nameFunction = "GET_all_item_that_are_part_of_the_upper_nav_menu"
        navBarMenu = self.soup.find_all("table", {"id": f"menu-table"})
        for elements in navBarMenu:
            for subelement in elements.find_all("div"):
                div = subelement.string
                if div is not None:
                    div = str(div).strip()
                    print(f"- {div}")

    def findHref(self):
        self.nameFunction = "find_all_properties_that_have_href "
        hrefs = ""
        for href in self.soup.find_all(href=True):
            hrefs += f" - {href}\n"
        self.myhrefs = self.checkIfThirty(hrefs, self.nameFunction)
        return print(f"GET the href and print it: {self.myhrefs}")
        #return print(f"find all properties that have href <{self.hrefs}>")



    def getUFMMailButton(self):
        self.nameFunction = "GET_href_of_UFMail_button"
        #for a in self.soup.find_all('a'):
        #    if a.text == "UFMAil":
        #        self.linkButtonMail = a.get('href')
        #return print(f"Get href of UFMail Button: <{self.linkButtonMail}>")
        for a in self.soup.find_all('a'):
            if (a.text == "UFMail"):
                linkButtonMail = a.get('href')
        return print(f"GET href of UFMail button: < {linkButtonMail} >")

    def getMiUButton(self):
        self.nameFunction = "GET_href_of_MiU_button"
        #for a in self.soup.find_all('a'):
        #    if a.text == "UFMAil":
        #        self.linkButtonMail = a.get('href')
        #return print(f"Get href of UFMail Button: <{self.linkButtonMail}>")
        for a in self.soup.find_all('a'):
            if (a.text == "MiU"):
                linkButtonMiU = a.get('href')
        return print(f"GET href of MiU button: < {linkButtonMiU} >")

    def getHrefImg(self):
        for img in self.soup.find_all('a'):
            x = len(img.find_all('img'))
            if (x > 0):
                print("- " + img.get('href'))

    def countA(self):
        self.countAllA = len(self.soup.find_all('a', href=True))
        return print(f"Count all <a>: {self.countAllA}")

    def crateCSVFile(self):
        a = self.soup.find_all("a")
        csvFile = open("extra_as.csv", "w")
        w = csv.writer(csvFile)
        for i in a:
            data = ['Text: ' + i.get_text(), ' href: ' + i['href']]
            w.writerow(data)
        csvFile.close()
        shutil.move(f'extra_as.csv', 'logs')
        return print("Archivo con texto y hrefs creado, guardado en carpeta log")

print("1. Portal")
portalazo = portal()
print("-"*60)
portalazo.getTitle()
print("-"*60)
portalazo.getAddress()
print("-"*60)
portalazo.getPhoneEmail()
print("-"*60)
portalazo.getUpenNavElements()
print("-"*60)
portalazo.findHref()
print("-"*60)
portalazo.getUFMMailButton()
print("-"*60)
portalazo.getMiUButton()
print("-"*60)
portalazo.getHrefImg()
print("-"*60)
portalazo.countA()
print("-"*60)
portalazo.crateCSVFile()