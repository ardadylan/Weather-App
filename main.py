import datetime as dt
import requests


BASE_URL = "https://api.openweathermap.org/data/2.5/weather?"
API_KEY = open('api_key', 'r').read()
CITY = "Fairfax"

url = BASE_URL + "appid=" + API_KEY + "&q=" + CITY
response = requests.get(url).json()



def kelvin_to_celsius_fahrenheit(kelvin):
    celsius = kelvin - 273.15
    fahrenheit = celsius * (9/5) + 32
    return celsius, fahrenheit


temp_kelvin = response['main']['temp']
temp_celsius, temp_fahrenheit = kelvin_to_celsius_fahrenheit(temp_kelvin)
feels_like_kelvin = response[ 'main']['feels_like']
feels_like_celsius, feels_like_fahrenheit = kelvin_to_celsius_fahrenheit(feels_like_kelvin)
wind_speed = response['wind']['speed']
humidity = response['main']['humidity']
description = response['weather'][0]['description']
sunrise_time = dt.datetime.fromtimestamp(response['sys']['sunrise'] + response['timezone'], dt.UTC)
sunset_time = dt.datetime.fromtimestamp(response['sys']['sunset'] + response['timezone'], dt.UTC)


print(f"Temperature in {CITY}: {temp_celsius:.2f}C   or  {temp_fahrenheit:.2f}F")
print(f"Temperature feels like {feels_like_celsius:.2f}C   or  {feels_like_fahrenheit:.2f}F")
print(f"Humidity: {humidity}%")
print(f"Wind Speed: {wind_speed}m/s")
print(f"Sunrise at {sunrise_time} local time")
print(f"Sunrise at {sunset_time} local time")
print(f"General Weather in City {description}")
