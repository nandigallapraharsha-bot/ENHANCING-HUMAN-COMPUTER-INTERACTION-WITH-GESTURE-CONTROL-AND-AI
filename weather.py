import requests

api_key = ''  # Replace with your OpenWeatherMap API key
api_address = f'http://api.openweathermap.org/data/2.5/weather?id=524901&appid={api_key}'

def temp():
    json_data = requests.get(api_address).json()  # Retrieve API response
    temperature = round(json_data["main"]["temp"] - 273, 1)
    return temperature

def des():
    json_data = requests.get(api_address).json()  # Retrieve API response
    description = json_data["weather"][0]["description"]
    return description


