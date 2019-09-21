from bs4 import BeautifulSoup
import requests,sys

class inspect_html:

    def parser(self):
        try:
            self.html_content = requests.get(self.url).text
        except:
            print(f"unable to get {self.url}")
            sys.exit(1)

        self.soup = BeautifulSoup(self.html_content, "html.parser")

    def url_portal(self):
        self.urlportal == "http://ufm.edu/Portal"