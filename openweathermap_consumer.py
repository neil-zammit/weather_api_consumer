import requests

# api key: f106e61bbc4dd9e010867800ea00bc45

# API Calls for 5 different cities
request_fgura = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Fgura,mt&appid=f106e61bbc4dd9e010867800ea00bc45')
request_london = requests.get('http://api.openweathermap.org/data/2.5/weather?q=London,uk&appid=f106e61bbc4dd9e010867800ea00bc45')
request_sanfrancisco = requests.get('http://api.openweathermap.org/data/2.5/weather?q=San Francisco,us&appid=f106e61bbc4dd9e010867800ea00bc45')
request_tokyo = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Tokyo,jp&appid=f106e61bbc4dd9e010867800ea00bc45')
request_shanghai = requests.get('http://api.openweathermap.org/data/2.5/weather?q=Shanghai,cn&appid=f106e61bbc4dd9e010867800ea00bc45')

# Parsing API call results in json and assigning to variables
fgura_weather = request_fgura.json()
london_weather = request_london.json()
sanfrancisco_weather = request_sanfrancisco.json()
tokyo_weather = request_tokyo.json()
shanghai_weather = request_shanghai.json()

# Appending json variables to common list
weather_list = [fgura_weather, london_weather, sanfrancisco_weather, tokyo_weather, shanghai_weather]

# Create a list of dictionaries with keys name and temp
temp_list_dict = []  # empty list to store dictionaries of name and temp

for i in weather_list:
    temp_list_dict.append({
                 'name': i['name'],
                 # Store temp in °C
                 # 0 Kelvin = -273.15°C
                 'temp': round(i['main']['temp'] - 273.15, 2)  # answer rounded to 2dp
             })


# Functions


def return_temp():
    """
    Returns the list of cities and their temperatures in °C
    """
    for i in temp_list_dict:
        print(f"The temperature in {i['name']} is {i['temp']}°C")
    return ''


def warmest_city():
    """
        Returns the city with the warmest temperature in °C
    """
    warmest = temp_list_dict[0]['temp']  # set warmest to first city/temp in list
    for x in temp_list_dict:
        for i in temp_list_dict:
            if i['temp'] > warmest:
                warmest = i['temp']

        if warmest == x['temp']:
            return f"The warmest city is {x['name']}, with a temperature of {x['temp']}°C"


def coldest_city():
    """
        Returns the city with the coldest temperature in °C
    """
    coldest = temp_list_dict[0]['temp']  # set coldest to first city/temp in list
    for x in temp_list_dict:
        for i in temp_list_dict:
            if i['temp'] < coldest:
                coldest = i['temp']
        if coldest == x['temp']:
            return f"The coldest city is {x['name']}, with a temperature of {x['temp']}°C"


# Function Calls
print(return_temp())
print(warmest_city())
print(coldest_city())
