import urllib.request
import json
import os
from django.shortcuts import render

# Get API key from environment variable
WEATHER_API_KEY = os.getenv('WEATHER_API_KEY', 'c8792b018609d253fe5181cd4f6e7677')  # Fallback to demo key

def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        try:
            source = urllib.request.urlopen(
                f'http://api.openweathermap.org/data/2.5/weather?q={city}&units=metric&appid={WEATHER_API_KEY}'
            ).read()
            
            list_of_data = json.loads(source)

            data = {
                "country_code": str(list_of_data['sys']['country']),
                "coordinate": str(list_of_data['coord']['lon']) + ', '
                + str(list_of_data['coord']['lat']),
                "temp": str(list_of_data['main']['temp']) + ' °C',
                "pressure": str(list_of_data['main']['pressure']),
                "humidity": str(list_of_data['main']['humidity']),
                'main': str(list_of_data['weather'][0]['main']),
                'description': str(list_of_data['weather'][0]['description']),
                'icon': list_of_data['weather'][0]['icon'],
            }
        except Exception as e:
            data = {
                'error': 'Error fetching weather data. Please check the city name and try again.'
            }
    else:
        data = {}

    return render(request, "main/index.html", data)
