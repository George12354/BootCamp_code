import requests


def question_data():
    response = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean&category=18")
    response.raise_for_status()
    data = response.json()
    variable = data["results"]

    return variable


question_data = question_data()
