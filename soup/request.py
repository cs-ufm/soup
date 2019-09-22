# imports
from bs4 import BeautifulSoup
import requests,sys,csv,json
class Request:

    #method to define url and make the get verb using requests 
    def makeGet(self,url):

        #url="http://ufm.edu/Portal"
        # Make a GET request to fetch the raw HTML content
        try:
            html_content = requests.get(url).text
        except:
            print(f"unable to get {url}")
            sys.exit(1)

        # Parse the html content, this is the Magic ;)
        soup = BeautifulSoup(html_content, "html.parser")

        #return the object
        return soup