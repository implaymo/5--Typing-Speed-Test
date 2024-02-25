import requests


class RandomWords():
    def __init__(self) -> None:
        self.response = requests.get("https://random-word-api.herokuapp.com/word?number=10&lang=en")
        self.response.raise_for_status()
        self.words_list = self.response.json()  # Use json() to parse the response as a JSON list

    def all_words_printed(self):
        return " ".join(self.words_list)
   
