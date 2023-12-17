#!/usr/bin/python3

import string
import requests
import datetime

from Verbal import Verbal
import api_secrets

verbal = Verbal()

class Weather:
	def __init__(self):
		pass
		
	def kelvin_to_celsius_fahrenheit(self, kelvin):
		celsius = kelvin - 273.15
		fahrenheit = celsius * (9/5) + 32
		return celsius, fahrenheit


	def getWeather(self, city):
		print(city)
		city = city.translate(str.maketrans('','',string.punctuation))
		print(city)
		CITY = city
		try:
			openWeatherUrl = api_secrets.API_OPEN_WEATHER_BASE_URL + CITY
			#api_secrets.API_OPEN_WEATHER_BASE_URL + "appid=" + api_secrets.API_KEY_OPEN_WEATHER + "&q=" + CITY

			response = requests.get(openWeatherUrl).json()
			temp_kelvin = response['main']['temp']
			temp_celsius, temp_fahrenheit = self.kelvin_to_celsius_fahrenheit(temp_kelvin)
			feels_like_kelvin = response['main']['feels_like']
			feels_like_celsius, feels_like_fahrenheit = self.kelvin_to_celsius_fahrenheit(feels_like_kelvin)
			wind_speed = response['wind']['speed']

			humidity = response['main']['humidity']
			description = response['weather'][0]['description']
			sunrise_time = datetime.datetime.utcfromtimestamp(response['sys']['sunrise'] + response['timezone'])
			sunset_time = datetime.datetime.utcfromtimestamp(response['sys']['sunset'] + response['timezone'])

			weather = f"The temperature in {CITY} is currently {temp_fahrenheit:.2f} degrees Fahrenheit. It feels like {feels_like_fahrenheit:.2f} degrees Fahrenheit. The humidity in {CITY} is at {humidity}% and the wind speed is blowing at {wind_speed}m/s. The general weather in {CITY} is {description}."
		# Additionally, the sun rises in {CITY} at {sunrise_time} and sets at {sunset_time} local time. " 
			return weather
		except KeyError:
			return "I'm sorry, I did not hear the name of a city."
		except AssertionError:
			return "I'm sorry, I did not hear the name of a city."


	def getTemperature(self, city):
		print(city)
		city = city.translate(str.maketrans('','',string.punctuation))
		print(city)
		CITY = city
		
		try:
			openWeatherUrl = api_secrets.API_OPEN_WEATHER_BASE_URL + CITY
			#api_secrets.API_OPEN_WEATHER_BASE_URL + "appid=" + api_secrets.API_KEY_OPEN_WEATHER + "&q=" + CITY


			response = requests.get(openWeatherUrl).json()
			temp_kelvin = response['main']['temp']
			temp_celsius, temp_fahrenheit = self.kelvin_to_celsius_fahrenheit(temp_kelvin)
			feels_like_kelvin = response['main']['feels_like']
			feels_like_celsius, feels_like_fahrenheit = self.kelvin_to_celsius_fahrenheit(feels_like_kelvin)
			temperature = f"The temperature in {CITY} is currently {temp_fahrenheit:.2f} degrees Fahrenheit. It feels like {feels_like_fahrenheit:.2f} degrees Fahrenheit."
			return temperature
		except KeyError:
			return "I'm sorry, I did not hear the name of a city."
		except AssertionError:
			return "I'm sorry, I did not hear the name of a city."


	def removePunctuation(input):
		translator = str.maketrans("","",string.punctuation)
		result = input.translate(translator)
		return result
