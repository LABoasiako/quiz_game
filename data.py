import requests

url = "https://opentdb.com/api.php?amount=10&category=11&type=boolean"
trivia_api = requests.get(url).json()

question_data = trivia_api["results"]
