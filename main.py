import argparse
import pyfiglet
import requests
from simple_chalk import chalk

# API key for openweathermap
API_KEY = "afa65a52c9618fe41bef4e30346a59d5"

# Base URL for openweathermap API
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


WEATHER_ICONS = {
	# day icons
	"01d": "☀️",
	"02d": "⛅️",
	"03d": "☁️",
	"04d": "☁️",
	"09d": "🌧",
	"10d": "🌦",
	"11d": "⛈",
	"13d": "❄️",
	"50d": "🌫",
	# night icons
	"01n": "🌙",
	"02n": "⛅️",
	"03n": "☁️",
	"04n": "☁️",
	"09n": "🌧",
	"10n": "🌦",
	"11n": "⛈",
	"13n": "❄️",
	"50n": "🌫",
    
}

parser = argparse.ArgumentParser(description="Check the weather for a certain country/city")
parser.add_argument("country", help="The country/city to check the weather for")
args = parser.parse_args()
url = f"{BASE_URL}?q={args.country}&appid={API_KEY}&units=metric"

# Make API request and parse response using requests module
response = requests.get(url)
if response.status_code != 200:
	print(chalk.red("Error: Unable to retrieve weather information"))
	exit()

# Parsing the JSON response from the API and extracting the weather data.
data = response.json()

# Get information from response
temperature = data["main"]["temp"]
feels_like = data["main"]["feels_like"]
description = data["weather"][0]["description"]
icon = data["weather"][0]["icon"]
city = data["name"]
country = data["sys"]["country"]

# Print the weather data
weather_icon = WEATHER_ICONS.get(icon, "")
output = f"{pyfiglet.figlet_format(city)}, {country}\n\n"
output += f"{weather_icon} {description}\n"
output += f"Temperature: {temperature}°C\n"
output += f"Feels like: {feels_like}°C\n"

# Print the output
print(chalk.green(output))