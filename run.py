import random
words_to_guess = ["cucamber"]
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
    """
    Get a symbol / letter input from user.
    validate that it hasnt been used before 
    validate that there is not more than one symbol entered
    and entery is a letter
    """
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

def replace_letter(hidden, visible, letter):
    """
    Replace a symbol * in the hidden word,
    in the place where should be the guessed letter.
    in case the guessed letter contains the word 
    """
    num = 0
    for symb in visible:
        if symb == letter:
            hidden = hidden[:num] + letter + hidden[num + 1:]
        num += 1
    return hidden


word = get_words(words_to_guess)
secret = hidden_word(word)
letter = guess_letter()
test = replace_letter(secret, word, letter)
print(word)
print(secret)
print(test)