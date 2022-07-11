from email import message
import requests
from twilio.rest import Client

API_KEY = '91b1913f192364d6cc0d00db3d4d206e'
ACCOUNT_SID = 'AC04515352dbf7f1abc560983c3ba25dde'
AUTH_TOKEN = '52dfee836de193473dea7e980bdc3294'
LONG = 21.01178
LAT = 52.229771

parameters = {
    'lat': LAT,
    'lon': LONG,
    'appid': API_KEY,
    'exclude': 'current,minutely,daily'
}

response = requests.get('https://api.openweathermap.org/data/2.5/onecall', params=parameters)
response.raise_for_status()
weather_data = response.json()

weather_slice = weather_data['hourly'][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data['weather'][0]['id']
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella",
        from_='+13254408878',
        to='+48731565334'
    )

print(message.status)