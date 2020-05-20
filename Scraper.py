'''kivy looks like best bet for gui'''

import requests
import time
from bs4 import BeautifulSoup, NavigableString
#gobal variables for temp, cloud condition, temp celcius

#Update fucntion


class Scraper:

    def __init__(self, url):
        self.page = requests.get(url)
        self.soup = BeautifulSoup(self.page.content, 'html.parser')
        self.temp_F = 0
        self.temp_C = 0
        self.cloud = "" 



    def getData(self):
        results = self.soup.find(id="current-conditions-body")
        self.temp_F = results.find('p', class_='myforecast-current-lrg').text
        print(self.temp_F)
        self.temp_C = results.find('p', class_='myforecast-current-sm').text
        print(self.temp_C)
        self.cloud = results.find('p', class_='myforecast-current').text
        print(self.cloud)    

if __name__ == "__main__":
    while(True):
        scraper = Scraper("https://forecast.weather.gov/MapClick.php?lat=41.467431900000065&lon=-81.53766429999996")
        scraper.getData()
        time.sleep(3*60*60)
