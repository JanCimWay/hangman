import random
words_to_guess = ["animal", "dog", "cat", "Cucamber", "apple", "table", "kitchen", "Mushrooms"]

def get_words(list):
    asked_word = list[random.randrange(len(list))]
    return asked_word

word = get_words(words_to_guess)
print(word)
