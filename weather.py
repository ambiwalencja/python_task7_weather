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


class Weather:
    def __init__(self, url, town, days):
        self.url = url
        self.town = town
        self.date = datetime.datetime.strptime(sys.argv[2], "%Y-%m-%d").date()
        self.forecast_length = days
        self.data = self.get_data()  # data will be in json format

    def check_date(self):
        difference = self.date - datetime.datetime.today().date()
        if difference.days > 10:
            return False
        if difference.days < 0:
            return False
        return True

    def get_data(self):
        if not self.check_date():
            return False
        api_key = sys.argv[1]
        request_params = {'key': api_key, 'q': self.town, 'days': self.forecast_length, 'dt': self.date}
        response = requests.get(self.url, params=request_params)
        # pprint.pprint(response.json())
        return response.json()

    def get_rain_info(self):
        rain = self.get_data()['forecast']['forecastday'][0]['day']['daily_will_it_rain']
        return rain

    def get_snow_info(self):
        snow = self.get_data()['forecast']['forecastday'][0]['day']['daily_will_it_snow']
        return snow

    def write_to_file(self):
        with open("forecast.txt", "a") as file:
            file.write(f'{self.date},{self.get_rain_info()},{self.get_snow_info()}\n')


# print("Hello. This program will tell you if it will rain or snow in Warsaw"
#       "on given day up to 10 days from now. To get information about chosen day type"
#       "your secret code (API key) and the date in format YYYY-MM-DD. Enjoy!")

my_weather = Weather("http://api.weatherapi.com/v1/forecast.json", "Warsaw", 10)
if not my_weather.data:
    print("Couldn't load data. Please select date between today and 10 days forward.")
else:
    if my_weather.get_rain_info():
        print("It will rain.")
    if my_weather.get_snow_info():
        print("It will snow.")
    if not my_weather.get_rain_info() and not my_weather.get_snow_info():
        print("It will be clear.")
    my_weather.write_to_file()

# print(my_data.data)


# api_key = sys.argv[1]
# # town = sys.argv[2]
# town = 'Warsaw'
# date = datetime.datetime.strptime(sys.argv[2], "%Y-%m-%d").date()
#
# request_params = {'key': api_key,
#                   'q': town,
#                   'days': 10,
#                   'dt': date}
# resp = requests.get("http://api.weatherapi.com/v1/forecast.json", params=request_params)


# will_it_rain = resp.json()['forecast']['forecastday'][0]['day']['daily_will_it_rain']
# will_it_snow = resp.json()['forecast']['forecastday'][0]['day']['daily_will_it_snow']
# # will_it = 0
# if not will_it_rain and not will_it_snow:
#     # will_it = 0
#     print('It will neither rain nor snow.')
# else:
#     print("It will rain or snow.")
#
# with open("forecast.txt", "a") as file:
#     file.write(f'{date},{will_it_rain},{will_it_snow}\n')





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
