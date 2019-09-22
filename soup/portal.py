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
        print(soup.title)
        print(soup.title.string)
        
        return result

    