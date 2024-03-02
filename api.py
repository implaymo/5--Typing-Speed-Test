import requests
import os
from dotenv import load_dotenv

load_dotenv()


class RandomWords():
    def __init__(self) -> None:
        api_key = os.getenv("api_key")
        self.response = requests.get("https://api.api-ninjas.com/v1/loremipsum?paragraphs=1", headers={'X-Api-Key': api_key})
        self.response.raise_for_status()
        data = self.response.json()
        self.words_list = data.get("text", "").split()

    def all_words(self, words_list):
        return " ".join(words_list)
   
 