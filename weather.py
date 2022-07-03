import requests
import math
import sys
from condition import *

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
        print("Failed") # Should be printing somewhere else, maybe on return.
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
    weather_description = weather["weather"]
    print(weather_description)
    print(weather)
    return weather["main"]["temp"]

def kelvin_to_celsius(temp_kelvin):
    return temp_kelvin - 273.15

def get_weather_icon(response: requests):
    '''
    Takes the JSON, maybe only the needed information should be passed?
    TODO: Determinate what icon should be displayed depending on if it's
    sunny, rainy, cloudy, thunderstorms or snowing.
    Returns the weather icon (ASCII ART)
    '''
    pass


def main():
    '''
    r = API response
    

     CITY_NAME = set_city_name().capitalize()
    

    if(request_validation(CITY_NAME, r)):
        temperature = get_weather(r)
        print(f"Temperature in {CITY_NAME}: {kelvin_to_celsius(temperature):.1f}C")

    '''
    CITY_NAME = set_city_name().capitalize()
    weather1 = condition(CITY_NAME)
        

    

if __name__ == "__main__":
    main()