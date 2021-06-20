import sys
import requests  # https://docs.python-requests.org/en/master/
import pprint  # pretty print https://docs.python.org/3/library/pprint.html
import datetime
from requests.auth import HTTPBasicAuth

# API Key: 57836734f5964a9a970213219211406
# https://stackoverflow.com/questions/53075939/calling-rest-api-with-an-api-key-using-the-requests-package-in-python
# https://www.weatherapi.com/
# tutaj info: https://www.weatherapi.com/docs/
# tutaj url: http://api.weatherapi.com/v1/forecast.json


# class GetData:
#     def __init__(self, url):
#         self.url = url
#         self.data = self.get_data()  # data will be in json format
#
#     def get_data(self, key):
#         resp = requests.get(self.url)
#         pprint.pprint(resp.json())
#         return resp.json()
#
#
# class Weather:
#     def __init__(self, date):
#         self.town = ''
#         self.date = date
#         self.time = ''


# my_data = GetData("http://api.weatherapi.com/v1/forecast.json")
# print(my_data.data)


api_key = sys.argv[1]
# town = sys.argv[2]
town = 'Warsaw'
date = datetime.datetime.strptime(sys.argv[2], "%Y-%m-%d").date()

request_params = {'key': api_key,
                  'q': town,
                  'days': 10,
                  'dt': date}
resp = requests.get("http://api.weatherapi.com/v1/forecast.json", params=request_params)


will_it_rain = resp.json()['forecast']['forecastday'][0]['day']['daily_will_it_rain']
will_it_snow = resp.json()['forecast']['forecastday'][0]['day']['daily_will_it_snow']
# will_it = 0
if not will_it_rain and not will_it_snow:
    # will_it = 0
    print('It will neither rain nor snow.')
else:
    print("It will rain or snow.")

with open("forecast.txt", "a") as file:
    file.write(f'{date},{will_it_rain},{will_it_snow}\n')





# date_string = '2021-06-25'
# api_key = '57836734f5964a9a970213219211406'
# town = 'Warsaw'

# weather_forecast = resp.json()
# print(weather_forecast)
# print("\n\n\n")
# helper_variable = input("type anything")

# jeśli już mamy info o jednym dniu, to zapisujemy je do pliku

# nie robić za dużo żądań naraz, jak chcemy, żeby nas nie wyrzuciło, to możemy uzyć time.sleep()

# resp = requests.get(url)
# resp.text
# resp.json()  # json to jest jakiś rodzaj słownika

# jakie klasy będą nam potrzebne?
# dostajemy to w jakimś formacie, i musimy zrobić to tak, żeby było czytelne
# klasa weather będzie nadrzędna
# pogoda dla jakiegoś miasta to będzie obiekt klasy weather, z atrybutami miasto, data, godzina
