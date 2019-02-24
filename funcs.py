import requests

def weather_api(name):

	api = "http://api.openweathermap.org/data/2.5/weather?appid=3009ca0332d7a9e8726110d3756acfb3&q="
	city_name = name
	url=api+city_name+ "&units=metric"
	return requests.get(url).json()