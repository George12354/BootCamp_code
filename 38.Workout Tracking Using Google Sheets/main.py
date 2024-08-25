import json
import requests
from datetime import datetime

Application_ID = "820b5ddd"
Application_Keys = "41956a11048eeed2f7ac2e1a26a0840b"

APP_Endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
endpoint = "https://api.sheety.co/79ce34afa9721efdecd0b8161146ee03/copyOfMyWorkouts/workouts"


APP_params = {
    "x-app-id": Application_ID,
    "x-app-key": Application_Keys
}


data = {
    'query': str(input("Tell me which exercise you did: "))  # Replace with the actual value
}


exercise_response = requests.post(url=APP_Endpoint, headers=APP_params, json=data)
session = exercise_response.json()
print(session)
# print(session["exercises"][0]["user_input"])

# Ran 2 miles and walked for 3kms.

# Stage 2---Spreadsheet Section

spreadsheet_url = 'https://api.sheety.co/79ce34afa9721efdecd0b8161146ee03/copyOfMyWorkouts/workouts'

today = datetime.now()

body = {
    'workout': {
        # Workout details
        "date": today.strftime("%Y/%m/%d"),
        "time": today.strftime("%X"),
        "exercise": session["exercises"][0]["user_input"].title(),
        "duration": session["exercises"][0]["duration_min"],
        "calories": session["exercises"][0]["nf_calories"]
    }
}

headers = {
    'Content-Type': 'application/json'
}

spreadsheet_response = requests.post(url=spreadsheet_url, headers=headers, data=json.dumps(body))
print(spreadsheet_response.text)
