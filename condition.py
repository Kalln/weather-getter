import requests
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

API_KEY = os.environ.get("API_KEY")

class condition:

    def request_weather(self, CITY_NAME):
        print(CITY_NAME)
        return requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}")

    def validate_request(self, code):
        if (code == 404):
            return False
        return True

    def get_user_weather(self):
        """
        Gets user friendly formatted weather and returns a dict?
        """
        weather_dict = {}
        # print(self.get_temp_celsius_fahrenheit())
        # print(self.json_weather)
        # print(self.get_feels_like_temp())
        # print(self.get_description())
        # print(self.get_sunrise_and_sunset())
        # print(self.get_country())
        # print(f"{self.get_humidity()}%")
        return self.get_temp_celsius_fahrenheit()

    def get_temp_celsius_fahrenheit(self):
        kelvin_temp = self.json_weather["main"]["temp"]
        return self.kelvin_to_celsius(kelvin_temp)

    def get_feels_like_temp(self):
        return self.kelvin_to_celsius(self.json_weather["main"]["feels_like"])

    def kelvin_to_celsius(self, kelvin_temp):
        celsius_temp = kelvin_temp - 273.15
        fahrenheit_temp = celsius_temp * (9/5) + 32
        return [celsius_temp, fahrenheit_temp]

    def get_description(self):
        weather_temp = self.json_weather["weather"]
        description = weather_temp[0]["description"]
        return description

    def get_sunrise_and_sunset(self):
        sunrise = self.json_weather["sys"]["sunrise"]
        sunset = self.json_weather["sys"]["sunrise"]
        return [sunrise, sunset]

    def convert_to_readable_time(self):
        pass

    def get_country(self):
        return self.json_weather["sys"]["country"]

    def get_humidity(self):
        return self.json_weather["main"]["humidity"]
    

    def __init__(self, CITY_NAME):
        self.city = CITY_NAME
        self.raw_weather = self.request_weather(CITY_NAME) # requests object
        self.json_weather = self.raw_weather.json()
        print(self.raw_weather.status_code)
        self.validation = self.validate_request(self.raw_weather.status_code) # return false if 404 code
        temp_temp = self.get_user_weather()
        print(f"It's {temp_temp[0]:.1f}C ({temp_temp[1]:.1f}F) in {CITY_NAME}")
