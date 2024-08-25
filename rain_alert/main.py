import requests
import os
from twilio.rest import Client

account_sid = os.environ.get("TWILIO_ACCOUNT_SID")
auth_token = os.environ.get("TWILIO_AUTH_TOKEN")

Endpoint = "https://api.openweathermap.org/data/2.5/weather"
api_key = "8859200c41163be4f80f67994f7cb889"

# or you can use this approach
# response = requests.get(
#     url=f"https://api.openweathermap.org/data/2.5/weather?lat=6.524379&lon=3.3792061&appid={api_key}")


weather_params = {
    "lat": 6.524379,
    "lon": 3.3792061,
    "appid": api_key
}

response = requests.get(Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()

will_rain = False
nos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
# you can use this approach
# weather_slice = weather_data["hourly"][":12"]
# NB: weather_slice represent the variable nos.
for index in nos[0:12]:
    data = weather_data["hourly"][index]["weather"][0]["id"]
    if int(data) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It will rain today. Don't forget to use an umbrella ☔️",
        from_='the number generated from twilio',
        to='08147454714'
    )
    print(message.status)
