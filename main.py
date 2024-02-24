from api import RandomWords

random_words_provider = RandomWords()

words = random_words_provider.response.text

print(words)
