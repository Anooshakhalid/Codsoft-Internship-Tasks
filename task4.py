# task 4
# Weather forecast Application

# import date time and request
import requests
from datetime import datetime

# main look
print('╔══════════════════════════════════════════╗')
print('║       WEATHER FORECAST APPLICATION       ║')
print('╚══════════════════════════════════════════╝')

print('Select method by which you want to know weather')
print('1) By City Name\n2) By Zip Code & Country Code\n')
choice_1 = input('Enter the option no:')

# my actual API key
api_key = 'd2eae61a9dd11b21858134fe58a5d36c'

try:
    # if user want to know weather by city name
    if choice_1 == '1':
        location = input('Enter your city name: ')
        # API link from website
        complete_api_link = f"https://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"

    # if user want to know weather by city zipcode
    elif choice_1 == '2':
        zipcode = input('Enter Zip Code e.g 94040: ')
        countrycode = input('Enter Country Code e.g (US, PK): ')
        # API link from website
        complete_api_link = f'https://api.openweathermap.org/data/2.5/weather?zip={zipcode},{countrycode}&appid={api_key}'
    else:
        raise ValueError('Invalid choice')

    api_link = requests.get(complete_api_link)

    # 200 means that HTTP code is successful
    # Check the status code
    if api_link.status_code == 200:
        api_data = api_link.json()

        main_data = api_data['main']
        weather_data = api_data['weather'][0]

        temperature_kelvin = main_data['temp']
        temperature_celsius = temperature_kelvin - 273.15
        weather_description = weather_data['description']
        humidity = main_data['humidity']
        wind_speed = api_data['wind']['speed']

        date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

        # print format
        if choice_1 == '1':
            print("+__________________________________________________________________________+")
            print("|      WEATHER STATS FOR - {}  ||  {}".format(location.upper(), date_time), "          |")
            print("+--------------------------------------------------------------------------+")
        elif choice_1 == '2':
            print("+__________________________________________________________________________+")
            print("|      WEATHER STATS FOR - {}  ||  {}".format(zipcode, date_time), "           |")
            print("+--------------------------------------------------------------------------+")

        # print the details
        print('CURRENT FORECAST:')
        print(f"Temperature: {temperature_celsius:.2f}°C")
        print(f"Weather: {weather_description.capitalize()}")
        print(f"Humidity: {humidity}%")
        print(f"Wind Speed: {wind_speed} km/h")
        print("-----------****------------")
    else:
        print(f"HTTP Error: {api_link.status_code}")

# exception handling
except Exception as e:
    print(f"An error occurred: {e}")

