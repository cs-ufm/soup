#imports 
#from bs4 import BeautifulSoup
#import requests,sys,csv,json

#Portal class, all the requirements of the phase 1 are met here
import csv
class Portal:
    def __init__(self, soup):
        self.soup = soup
        self.arrayToPrint = []

    #init the process
    def init(self):
        return self.run(self.soup)

    #the method that actually make every parameter from Portal section
    def run(self, soup):
        result = []
        #print(soup.title)
        #print(soup.title.string)

        #get the title
        result.append(f"GET the title and print it: {soup.title.string}")
        result.append("---------------------------------------")

        #get the complete address
        footer = soup.find(id="footer")
        address = footer.find_all("div", class_="span4")
        result.append(f"GET the Complete Address of UFM: {address[0].strong.string + address[0].a.text}")
        result.append("---------------------------------------")        

        #get the pone number and email
        result.append(f"GET the phone number and info email: {address[1].a.text} - {address[1].find_all('a')[1].text}")
        result.append("---------------------------------------")   

        #get all items that are from (id: menu-table)
        result.append(f"GET all item that are part of the upper nav menu (id: menu-table): ")
        for i in soup.find(id="menu-table").find_all(class_="menu-key"):
            result.append("-"+i.text.strip())
        result.append("---------------------------------------")   

        #find all a that has href to somewhere
        result.append(f"find all properties that have href (link to somewhere)")
        soup.find_all("a")
        for i in soup.find_all(attrs={"href":True}):
            if i.text != "":
                result.append("-"+i.name.strip()+": "+i.text.strip())
        result.append("---------------------------------------")
                
        #get href ufmail
        result.append(f"GET href of \"UFMail\" button: {soup.find(id='ufmail_')['href']}")
        result.append("---------------------------------------")

        #get href miu
        result.append(f"GET href \"MiU\" button: {soup.find(id='miu_')['href']}")
        result.append("---------------------------------------")

        #get all src for all imgs
        result.append(f"GET hrefs of all <img>:")
        soup.find_all("img")
        for i in soup.find_all(attrs={"src":True}):
            result.append("-" + i['src'])
        result.append("---------------------------------------")

        #count all a
        result.append(f"count all <a>: {len(soup.find_all('a'))}")
        result.append("---------------------------------------")       

        #extra
        with open('../logs/extra_as.csv', 'w+') as csvfile:
            filewriter = csv.writer(csvfile, delimiter=',',
                                    quotechar='|', quoting=csv.QUOTE_MINIMAL)
            filewriter.writerow(['Text','href'])
            for i in soup.find_all('a'):
                filewriter.writerow([i.text, i["href"]])


        return result

    