import random
words_to_guess = ["animal", "dog", "cat", "Cucamber", "apple", "table", "kitchen", "Mushrooms"]

def get_words(list):
    asked_word = list[random.randrange(len(list))]
    return asked_word

def hidden_word(answer):
    hidden = "*" * len(answer)
    return hidden

word = get_words(words_to_guess)
hidden = hidden_word(word)

print(word)
print(hidden)
