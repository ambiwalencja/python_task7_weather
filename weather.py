import sys
import requests  # https://docs.python-requests.org/en/master/
import pprint  # pretty print https://docs.python.org/3/library/pprint.html
import datetime

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
        # self.data = self.get_data()  # data will be in json format
        self.rain = 0
        self.snow = 0
        self.get_data()

    def check_date(self):
        difference = self.date - datetime.datetime.today().date()
        if difference.days > 10:
            return False
        if difference.days < 0:
            return False
        return True

    def read_from_file(self):
        with open("forecast.txt", "r") as file:
            for line in file.readlines():
                date_in_line = datetime.datetime.strptime(line.split(",")[0], "%Y-%m-%d").date()
                if date_in_line == self.date:
                    self.rain = line.split(",")[1]
                    self.snow = line.split(",")[2].split("\n")[0]
                    return True
            return False

    def get_data(self):
        if not self.check_date():
            return False
        if self.read_from_file():
            return True
        api_key = sys.argv[1]
        request_params = {'key': api_key, 'q': self.town, 'days': self.forecast_length, 'dt': self.date}
        response = requests.get(self.url, params=request_params)
        self.rain = response.json()['forecast']['forecastday'][0]['day']['daily_will_it_rain']
        self.snow = response.json()['forecast']['forecastday'][0]['day']['daily_will_it_snow']
        # print(f'debug: rain {self.rain}, snow {self.snow}.')
        # pprint.pprint(response.json())
        # return response.json()
        self.write_to_file()
        return True

    # def get_rain_info(self):
    #     self.rain = self.get_data()['forecast']['forecastday'][0]['day']['daily_will_it_rain']
    #     return self.rain
    #
    # def get_snow_info(self):
    #     self.snow = self.get_data()['forecast']['forecastday'][0]['day']['daily_will_it_snow']
    #     return self.rain

    def write_to_file(self):
        with open("forecast.txt", "a") as file:
            file.write(f'{self.date},{self.rain},{self.snow}\n')


# print("Hello. This program will tell you if it will rain or snow in Warsaw"
#       "on given day up to 10 days from now. To get information about chosen day type"
#       "your secret code (API key) and the date in format YYYY-MM-DD. Enjoy!")

my_weather = Weather("http://api.weatherapi.com/v1/forecast.json", "Warsaw", 10)
if not my_weather.get_data():
    print("Couldn't load data. Please select date between today and 10 days forward.")
else:
    # print(f'debug 4: rain {my_weather.rain}, snow {my_weather.snow}.')
    if int(my_weather.rain) == 1:
        # print(f'debug 2: rain {my_weather.rain}, snow {my_weather.snow}.')
        print("It will rain.")
    if int(my_weather.snow) == 1:
        # print(f'debug 3: rain {my_weather.rain}, snow {my_weather.snow}.')
        print("It will snow.")
    if int(my_weather.rain) == 0 and int(my_weather.snow) == 0:
        print("It will be clear.")
    # my_weather.write_to_file()

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
