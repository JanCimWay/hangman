import random
words_to_guess = ["animal", "dog", "cat", "Cucamber", "apple", "table", "kitchen", "Mushrooms"]
guessed_letters = []

def get_words(list):
    """
    Get a random word from list of words
    """
    asked_word = list[random.randrange(len(list))]
    return asked_word

def hidden_word(answer):
    """
    Create a hidden word - a string that consists of same amount
    of symbols as the word, but letters are repalced with *
    """
    hidden = "*" * len(answer)
    return hidden

def guess_letter():
    while True:
        try:
            letter = input("Enter letter: \n")
            if letter.isalpha() is False:
                raise ValueError ("Only latin letters are allowed!")
            elif len(letter) != 1:
                raise ValueError ("You must enter only one symbol!")
            elif letter in guessed_letters:
                raise ValueError ("You have already used this letter for guess")
            else:
                return letter
        except ValueError as e:
            print(e)

guess_letter()

"""
word = get_words(words_to_guess)
hidden = hidden_word(word)

print(word)
print(hidden)
"""