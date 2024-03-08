import random
words_to_guess = ["cucamber"]
guessed_letters = ["u"]
HANGMANPICS = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']

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
            letter = input("Enter letter: \n").upper()
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

def status_bar(word, result, score):
    """
    Status bar or result of game progress!
    """
    print(word)
    print(result)
    print(guessed_letters)
    print(HANGMANPICS[score])
    print("You have made " + str(score) + "mistakes till now!")
    print("\n")

def get_welcome_msg():
    print("welcome")


