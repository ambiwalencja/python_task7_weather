import requests
import pprint  # pretty print
import datetime
from requests.auth import HTTPBasicAuth


# nie robić za dużo żądań naraz, jak chcemy, żeby nas nie wyrzuciło, to możemy uzyć time.sleep()

# resp = requests.get(url)
# resp.text
# resp.json()  # json to jest jakiś rodzaj słownika

# jakie klasy będą nam potrzebne?
# dostajemy to w jakimś formacie, i musimy zrobić to tak, żeby było czytelne
# klasa weather będzie nadrzędna
# pogoda dla jakiegoś miasta to będzie obiekt klasy weather, z atrybutami miasto, data, godzina


class GetData:
    def __init__(self, url):
        self.url = url
        self.data = self.get_data()

    def get_data(self):
        resp = requests.get(self.url)
        pprint.pprint(resp.json())
        return resp.json()


class Weather:

    def __init__(self):
        self.town = ''
        self.date = ''
        self.time = ''

