import json
import requests

# How to get the data from the spreadsheet

url = 'https://api.sheety.co/79ce34afa9721efdecd0b8161146ee03/copyOfMyWorkouts/workouts'

response = requests.get(url=url)
print(response.text)


# How to post data to the spreadsheet
# spreadsheet_url = 'https://api.sheety.co/79ce34afa9721efdecd0b8161146ee03/copyOfMyWorkouts/workouts'
# body = {
#     'workout': {
#         # Workout details
#         "date": "21/07/2020",
#         "time": "15:00:00",
#         # "exercise": session["exercises"][0]["user_input"],
#         # "duration": session["exercises"][0]["duration_min"],
#         # "calories": session["exercises"][0]["nf_calories"]
#     }
# }
#
# headers = {
#     'Content-Type': 'application/json'
# }
#
# spreadsheet_response = requests.post(url=spreadsheet_url, headers=headers, data=json.dumps(body))
# print(spreadsheet_response.text)
