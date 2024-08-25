# What is an API?
# An Application Programming Interface(API) is a set of commands, functions, protocols, and objects that
# programmers can use to create software or interact with an external system.
# Is more like the interface between my program and the external system.

# API Endpoint is more like the location of the stored data.
# API Request: retrieve data without any form of authentication.

import requests
from datetime import datetime

MY_LAT = 32.715736  # Your latitude
MY_LONG = -117.161087  # Your longitude

response = requests.get(url="http://api.open-notify.org/iss-now.json")
# # The code below is to raise an exception if the response code is not successful(response code:200)
response.raise_for_status()

data = response.json()
print(data)

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)
# use latlong.net to check for the coordinate of the earth.
print(iss_position)

# parameters = {
#     "lat": MY_LAT,
#     "lng": MY_LONG,
#     "formatted": 0,
# }
#
# response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
# response.raise_for_status()
# data = response.json()
# sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
# sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
#
# print(sunrise)
# print(sunset)
#
# time_now = datetime.now()
#
# print(time_now.hour)
