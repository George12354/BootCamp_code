import json
import requests
from datetime import datetime, timedelta
from flight_data import FlightData


APP_Endpoint = "https://api.flightapi.io/iata/6683f3512753994faa3a5635"
Round_Trip_Endpoint = "https://api.flightapi.io/roundtrip"
sheety_doc_endpoint = "https://api.sheety.co/79ce34afa9721efdecd0b8161146ee03/copyOfFlightDeals/prices/2"

# iterate the city names
flight_params = {
    'name': "Frankfurt",
    'type': 'airport'
}


response = requests.get(url=APP_Endpoint, params=flight_params)
code = response.json()
print(code)

body = {
    'price': {
        "iataCode": code['data'][0]['iata']
        # spread_sheet details
    }
}

spread_sheet_header = {
    'Content-Type': 'application/json'
}

spreadsheet_response_1 = requests.put(url=sheety_doc_endpoint, headers=spread_sheet_header, data=json.dumps(body))
print(spreadsheet_response_1.text)


day = datetime.now()
tomorrow = day.day+1
months = day.month
print(months*timedelta(days=30))

round_trip_param = {
    "api_key": "6683f3512753994faa3a5635",
    "departure_airport_code": "LON",
    "arrival_airport_code": code['data'][0]['iata'],
    "departure_date": day.strftime(f"%Y/%m/{tomorrow}"),
    "arrival_date": day.strftime(f"%Y/%m/{tomorrow + 7}"),
    "number_of_adults": 2,
    "number_of_childrens": 1,
    "number_of_infants": 0,
    "cabin_class": "economy",
    "currency": "USD"
}


# url = "https://api.sheety.co/79ce34afa9721efdecd0b8161146ee03/copyOfFlightDeals/prices"
#
response = requests.get(url=Round_Trip_Endpoint, params=round_trip_param)
dat = response.json()
print(dat)
