from api import RandomWords
from gui import Gui

random_words_provider = RandomWords()
gui = Gui()



words = random_words_provider.response.text

print(words)
