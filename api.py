import requests


class RandomWords():
    def __init__(self) -> None:
        
        self.response = requests.get("https://random-word-api.herokuapp.com/word?number=10&lang=en")
        self.response.raise_for_status()  

