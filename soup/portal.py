#imports 
#from bs4 import BeautifulSoup
#import requests,sys,csv,json

#Portal class, all the requirements of the phase 1 are met here
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

        return result

    