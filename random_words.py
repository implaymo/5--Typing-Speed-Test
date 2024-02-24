import requests

response = requests.get("https://random-word-api.herokuapp.com/word?lang=es")
response.raise_for_status()

data = response.text

print(data)