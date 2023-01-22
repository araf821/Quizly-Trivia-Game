import requests

URL = "https://opentdb.com/api.php?amount=10&type=boolean"

response = requests.get(url=URL)
response.raise_for_status()

# print(response.json()["results"])

question_data = response.json()["results"]
