#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests,sys, csv, json, time
import os

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
        file = open(f"/logs/{nameOfFile}", "w")
        file.write(lines)
        file.close()

    def getCheckIfThirty(self, lines):
        return (len(lines.split('\n')) > 30)

    def checkIfThirty(self, lines, func):
        if self.getCheckIfThirty(lines):
            #self.logError(lines)
            self.nameOfOutputLogFile = f"logs/1portal_{func}.txt"
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



portalazo = portal()

portalazo.getTitle()
print("-"*60)
portalazo.getAddress()
print("-"*60)
portalazo.getPhoneEmail()
print("-"*60)