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
        self.nameFunction = "emails"
        mailList = [f"{mail.get('href')}".replace("mailto:", "", -1) for mail in
                    self.soup.find_all("a", href=re.compile(r"^mailto:"))]
        mailList.sort()
        mailListStr = ""
        for eachMail in mailList:
            mailListStr += f" - {eachMail}\n"
        self.myhrefs = self.checkIfThirty(mailListStr, self.nameFunction)
        return print(f"GET the href and print it: {self.myhrefs}")

    def vowelEmails(self):
        self.nameFunction = "emails_with_vowels"
        mailList = [f"{mail.get('href')}".replace("mailto:", "", -1) for mail in
                    self.soup.find_all("a", href=re.compile(r"^mailto:"))]
        vocales = ['a', 'e', 'i', 'o', 'u']
        count = 0
        for correos in mailList:
            if correos[0] in vocales:
                count += 1
        return print(f"La cantidad de correos que inician en vocal es {count}")

    def groupInAJSON(self):
        edificios = {}
        data = []
        tablas = self.soup.find_all("table", {'class': 'tabla ancho100'})
        for item in tablas[0].find_all('tr'):
            td = item.find_all('td')
            jsonify = []
            if len(td) == 5:
                building = td[4].text.strip().split(',')[0]
                facultad = td[0].text.strip()
                jsonify.append(building)
                jsonify.append(facultad)
                data.append(jsonify)
        for element in data:
            edificios[element[0]] = []
        for element in data:
            for j, k in edificios.items():
                if j == element[0]:
                    edificios[j].append(element[1])

        #Guardar JSON
        with open('4directorio_address.json', 'w+') as file:
            json.dump(edificios, file, ensure_ascii = False, indent = 4)
        shutil.move(f'4directorio_address.json', 'logs')
        return print("Sending output to: 4directorio_address.json")

    def correlateInAJSON(self):
        facultades = {}
        data = []
        tablas = self.soup.find_all("table", {'class': 'tabla ancho100'})
        for item in tablas[1].find_all('tr'):
            td = item.find_all('td')
            jsonify = []
            if len(td) == 3:
                decano = td[1].text.strip().split(',')[0]
                facultad = td[0].text.strip()
                email = td[2].text.strip()
                jsonify.append(decano)
                jsonify.append(facultad)
                jsonify.append(email)
                data.append(jsonify)
        for element in data:
            facultades[element[0]] = []
        for element in data:
            for j, k in facultades.items():
                if j == element[0]:
                    facultades[j].append(element[1])

        # Guardar JSON
        with open('4directorio_deans.json', 'w+') as file:
            json.dump(facultades, file, ensure_ascii=False, indent=4)
        shutil.move(f'4directorio_deans.json', 'logs')
        return print("Sending output to: 4directorio_deans.json")

    def crateCSVFileDirectory(self):
        elementosCSV = []
        tables = self.soup.find_all("table", {'class': 'tabla ancho100 col3'})
        #for elementos in tables:
          #  rawData = elementos.find_all('td')

        # for num in tables:
        #     #cont = 0
        #     cont = len(num)-1
        #     for datos in range(tables[cont].find_all('tr')):
        #         td = datos.find_all('td')
        #         temp = []
        #         if len(td) == 3:
        #             decano = td[1].text.strip().split(',')[0]
        #             facultad = td[0].text.strip()
        #             email = td[2].text.strip()
        #             temp.append(facultad)
        #             temp.append(decano)
        #             temp.append(email)
        #             elementosCSV.append(temp)
        #             #cont +=1

        # Consejo directivo
        for datos in tables[0].find_all('tr'):
            td = datos.find_all('td')
            temp = []
            if len(td) == 3:
                decano = td[1].text.strip().split(',')[0]
                facultad = td[0].text.strip()
                email = td[2].text.strip()
                temp.append(facultad)
                temp.append(decano)
                temp.append(email)
                elementosCSV.append(temp)

        # Decanos y directores
        for datos in tables[1].find_all('tr'):
            td = datos.find_all('td')
            temp = []
            if len(td) == 3:
                decano = td[1].text.strip().split(',')[0]
                facultad = td[0].text.strip()
                email = td[2].text.strip()
                temp.append(facultad)
                temp.append(decano)
                temp.append(email)
                elementosCSV.append(temp)

        # Directores de otras dependencias
        for datos in tables[2].find_all('tr'):
            td = datos.find_all('td')
            temp = []
            if len(td) == 3:
                decano = td[1].text.strip().split(',')[0]
                facultad = td[0].text.strip()
                email = td[2].text.strip()
                temp.append(facultad)
                temp.append(decano)
                temp.append(email)
                elementosCSV.append(temp)

        #Guardar CSV
        csvFile = open("4directorio_3column_tables.csv", "w")
        w = csv.writer(csvFile)
        #for elements in tables:
            #data = ['Entity: ' + elements.get_text(), ' FullName: ' + elements['href'], ' Email: ' + elements['mailto']]
        w.writerow(elementosCSV)
        csvFile.close()
        shutil.move(f'4directorio_3column_tables.csv', 'logs')
        return print("Sending output to 4directorio_3column_tables.csv creado, guardado en carpeta log")

print("="*60)
print("4. Directorio")
directoriazo = directorio()
directoriazo.getTitle()
print("-"*60)
directoriazo.sortEmails()
print("-"*60)
directoriazo.vowelEmails()
print("-"*60)
directoriazo.groupInAJSON()
print("-"*60)
directoriazo.correlateInAJSON()
print("-"*60)
directoriazo.crateCSVFileDirectory()