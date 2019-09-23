#!/usr/bin/env python3
from bs4 import BeautifulSoup
import requests,sys, csv, json, time, re
import os
import shutil

class directorio :
    url="https://www.ufm.edu/Directorio"
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
            self.nameOfOutputLogFile = f"4Directorio_{func}.txt"
            self.logFileWriter(lines, self.nameOfOutputLogFile)
            return f"Output exceeds 30 lines, sending output to: {self.nameOfOutputLogFile}"
        else:
            return f"{lines}"

    def getTitle(self):
        self.nameFunction = "GET_the_title_and_print_it"
        self.titles = self.checkIfThirty(directorio.soup.title.string, self.nameFunction)
        #self.titles = portal.soup.title.string
        return print(f"GET the title and print it: <{self.titles}>")

    def sortEmails(self):
        mailList = [f"{mail.get('href')}".replace("mailto:", "", -1) for mail in
                    self.soup.find_all("a", href=re.compile(r"^mailto:"))]
        mailList.sort()
        mailListStr = ""
        for eachMail in mailList:
            mailListStr += f" - {eachMail}\n"
        self.myhrefs = self.checkIfThirty(mailListStr, self.nameFunction)
        return (f"GET the href and print it: {self.myhrefs}")

print("4. Direcorio")
directoriazo = directorio()
directoriazo.getTitle()
print("-"*60)
directoriazo.sortEmails()