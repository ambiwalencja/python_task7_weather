import sys
import requests  # https://docs.python-requests.org/en/master/
import datetime


class Weather:
    def __init__(self, url, town, days):
        self.url = url
        self.town = town
        self.date = datetime.datetime.strptime(sys.argv[2], "%Y-%m-%d").date()
        self.forecast_length = days
        self.rain = 0
        self.snow = 0

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
        api_key = sys.argv[1]
        request_params = {'key': api_key, 'q': self.town, 'days': self.forecast_length, 'dt': self.date}
        response = requests.get(self.url, params=request_params)
        self.rain = response.json()['forecast']['forecastday'][0]['day']['daily_will_it_rain']
        self.snow = response.json()['forecast']['forecastday'][0]['day']['daily_will_it_snow']
        self.write_to_file()
        return True

    def write_to_file(self):
        with open("forecast.txt", "a") as file:
            file.write(f'{self.date},{self.rain},{self.snow}\n')


my_weather = Weather("http://api.weatherapi.com/v1/forecast.json", "Warsaw", 10)
if not my_weather.check_date():
    print("Couldn't load data. Please select date between today and 10 days forward.")
else:
    if not my_weather.read_from_file():  # if info is not in file
        my_weather.get_data()  # get gata from api
    if int(my_weather.rain) == 1:
        print("It will rain.")
    if int(my_weather.snow) == 1:
        print("It will snow.")
    if int(my_weather.rain) == 0 and int(my_weather.snow) == 0:
        print("It will be clear.")


