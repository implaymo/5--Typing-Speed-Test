import requests
import os
from dotenv import load_dotenv
import string

load_dotenv()


class RandomWords():
    def __init__(self) -> None:
        api_key = os.getenv("api_key")
        self.response = requests.get("https://api.api-ninjas.com/v1/loremipsum?paragraphs=1", headers={'X-Api-Key': api_key})
        self.response.raise_for_status()
        data = self.response.json()
        self.words_list = data.get("text", "").split()
        
    def all_words(self, words_list):
        self.words_paired_in_ten = [words_list[i:i+10] for i in range(0, len(words_list), 10)]
        return "\n".join([" ".join(self.remove_punctuation(words)) for words in self.words_paired_in_ten])

   
    def remove_punctuation(self, words):
        # Remove punctuation from every word of a list of words
        translator = str.maketrans("", "", string.punctuation)
        return [word.translate(translator) for word in words]