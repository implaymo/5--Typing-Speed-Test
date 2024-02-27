import requests


class RandomWords():
    def __init__(self) -> None:
        self.response = requests.get("https://random-word-api.herokuapp.com/word?lang=en&number=5&length=4")
        self.response.raise_for_status()
        self.words_list = self.response.json()  # Use json() to parse the response as a JSON list

    def all_words(self, words_list):
        return " ".join(words_list)
   
 