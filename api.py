import requests
import string



class RandomWords():
    def __init__(self) -> None:
       
        headers = {
                    "X-RapidAPI-Key": "970a65e5e8msh7b1396915084dc8p15bebfjsnb62b6e4fc80b",
                    "X-RapidAPI-Host": "paragraph-generator.p.rapidapi.com"
                }
        querystring = {"topic":"How to Make Your First Virtual Team Meeting a Success","section_heading":"How to keep track of what you've discussed"}
        
        self.response = requests.get("https://paragraph-generator.p.rapidapi.com/paragraph-generator", headers=headers, params=querystring)
        self.response.raise_for_status()
        data = self.response.json()
        self.words_list = data[0].split()

    def all_words(self, words_list):
        # Gets all words in a list of lists of 10 elements and return those words as a line of a paragraph 
        self.words_list
        self.words_paired_in_ten = [words_list[i:i+10] for i in range(0, len(words_list), 10)]
        return "\n".join([" ".join(self.remove_punctuation(words)) for words in self.words_paired_in_ten]).lower()

   
    def remove_punctuation(self, words):
        # Remove punctuation from every word of a list of words
        translator = str.maketrans("", "", string.punctuation)
        return [word.translate(translator) for word in words]