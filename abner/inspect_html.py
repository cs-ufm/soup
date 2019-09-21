from bs4 import BeautifulSoup
import requests,sys

class inspect_html:

    def url_portal(self):
        self.urlportal == "http://ufm.edu/Portal"

    def inspecter(self, url_to_inspect):
        try:
            html_content = requests.get(url_to_inspect).text
        except:
            print(f"unable to get {url_to_inspect}")
            sys.exit(1)

        soup = BeautifulSoup(html_content, "html.parser")