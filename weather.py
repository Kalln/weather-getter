import requests
import math
import sys
import os
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

API_KEY = os.environ.get("API_KEY")
CITY_NAME = None


def set_city_name():
    '''
    TERMINAL ARGUMENT HANDLING
    check if user entered city,
    if not will proceed with default city: STOCKHOLM.
    TODO: Implement possibility to request from multiple city
    TODO: Implement possibility to save weather on a txt file
    TODO: Implement possbility to give a text file with city names.
    '''
    if(len(sys.argv) < 2):
        return "Stockholm"
    else:
        return sys.argv[1]

# check status code
def request_validation(city: str, response: requests):
    '''returns false on 404 error code'''
    if(response.status_code == 404):
        return False
    else:
        return True


def get_weather(response: requests):
    '''
    gets weather (ONLY TEMPARUTE FOR NOW).
    TODO: check if cloudy, sunny, raining or thunderstorms
    TODO: return factorised list or dict with the needed information
    '''
    weather = response.json()
    return weather["main"]["temp"]

def kelvin_to_celsius(temp_kelvin):
    return temp_kelvin - 273.15


def main():
    CITY_NAME = set_city_name().capitalize()
    r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={CITY_NAME}&appid={API_KEY}")

    if(request_validation(CITY_NAME, r)):
        temperature = get_weather(r)
        print(f"Temperature in {CITY_NAME}: {kelvin_to_celsius(temperature):.1f}C")

if __name__ == "__main__":
    main()