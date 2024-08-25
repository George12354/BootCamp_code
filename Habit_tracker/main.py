import requests
from datetime import datetime

USERNAME = "geordie12"
TOKEN = "gasidjadvakdjfjghlsd"
GRAPH_ID = "graph0"

pixela_endpoint = 'https://pixe.la/v1/users'

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# step 1
# POST - Create a new user
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# step 2
# Create a graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "coding Graph",
    "unit": "min",
    "type": "int",
    "color": "shibafu"
}

# Use headers for more security 🔐
# and also as a means to authenticate your access
headers = {
    "X-USER-TOKEN": TOKEN
}
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

# To look at the graph, goto this url
# https://pixe.la/v1/users/geordie12/graphs/graph0.html


# step 3
# post a pixel

post_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime(year=2024, month=5, day=20)

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How long did you practice on how to code today? ")
}

# response = requests.post(url=post_pixel_endpoint, json=pixel_config, headers=headers)
# print(response.text)

# Using the put and delete HTTP Request

put_pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

put_pixel_config = {
    "quantity": "5"
}

response = requests.post(url=put_pixel_endpoint, json=put_pixel_config, headers=headers)
print(response.text)
