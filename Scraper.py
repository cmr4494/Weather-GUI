'''kivy looks like best bet for gui'''

import requests
from bs4 import BeautifulSoup, NavigableString


class Scraper:
    def __init__(self, url):
        self.page = requests.get(url)
        soup = BeautifulSoup(self.page.content, 'html.parser')
        results = soup.find(id="current-conditions-body")
        temperature_fahrenheit = results.find('p', class_='myforecast-current-lrg').text
        print(temperature_fahrenheit)
        temperature_celsius = results.find('p', class_='myforecast-current-sm').text
        print(temperature_celsius)
        phrase = results.find('p', class_='myforecast-current').text
        print(phrase)


if __name__ == "__main__":

    scraper = Scraper("https://forecast.weather.gov/MapClick.php?lat=41.467431900000065&lon=-81.53766429999996"
                      "#.Xrdb0qhKg2w")
