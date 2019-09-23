from bs4 import BeautifulSoup
import requests,sys

class inspectHtml:

    #url = "http://ufm.edu/Portal"

    def parser(self):
        self.url = "http://ufm.edu/Portal"
        try:
            self.html_content = requests.get(self.url).text
        except:
            print(f"unable to get {self.url}")
            sys.exit(1)

        self.soup = BeautifulSoup(self.html_content, "html.parser")

    def start(self):
        pass

  #  def urlPortal(self):
   #     self.urlportal == "http://ufm.edu/Portal"