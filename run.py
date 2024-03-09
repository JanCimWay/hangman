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
 /|\\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']

MENU = '''
MENU

To procced, You need to make Your choice.
Press the button according to Your wishes:

1 - Start the GAME
2 - Read instructions
3 - Quit

'''

INSTRUCTIONS = '''
INSTRUCTIONS

This game is called hangman.
We will choose for You a word from a list and You will
guess the word, letter by letter.
Your goal is to sovle the puzzle till the man is hanged

'''

WELCOME = '''
 _   _
| | | |
| |_| | __ _ _ __   __ _  __ _ _ __ ___   __ _ _ __
|  _  |/ _` | '_ \\ / _` |/ _` | '_ ` _ \\ / _` | '_ \\
| | | | (_| | | | | (_| | (_| | | | | | | (_| | | | |
\\_| |_/\\__,_|_| |_|\\__, |\\__,_|_| |_| |_|\\__,_|_| |_|
                    __/ |
                   |___/                             '''


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
                raise ValueError("Only latin letters are allowed!")
            elif len(letter) != 1:
                raise ValueError("You must enter only one symbol!")
            elif letter in guessed_letters:
                raise ValueError("You have already used this letter for guess")
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
    guessed_letters.append(letter)
    num = 0
    for symb in visible:
        if symb.upper() == letter.upper():
            hidden = hidden[:num] + letter.upper() + hidden[num + 1:]
        num += 1
    return hidden


def status_bar(word, result, score):
    """
    Status bar or result of game progress!
    """
    print("\n")
    print("--------------------------------------")
    print("YOUR CURRENT RESULT:")
    print(result)
    print("\n")
    print(HANGMANPICS[score])
    print("\n")
    print("Letters You have guessed till now: ")
    print(guessed_letters)
    print("You have made " + str(score) + " mistakes till now!")
    print("--------------------------------------")
    print("\n")


def game(name):
    """
    Clears the list of previosly guessed letters
    Gets from user word, replaces it with hidden word,
    Guess by guess counts the mistakes of the user.
    Updates the result and gets it back.
    """
    print("\n")
    print(name + " I hope You are ready! Let's start!")
    del guessed_letters[:]
    print("\n")
    mistakes = 0
    print(HANGMANPICS[mistakes])
    print("\n")
    word = get_words(words_to_guess)
    secret = hidden_word(word)
    guess = guess_letter()
    result = replace_letter(secret, word, guess)
    if result == secret:
        mistakes += 1
    status_bar(word, result, mistakes)
    while mistakes < (len(HANGMANPICS) - 1):
        guess = guess_letter()
        result = replace_letter(result, word, guess)
        step_mistakes = 0
        if result != word.upper():
            for symb in word:
                if symb.upper() != guessed_letters[-1].upper():
                    step_mistakes += 1
                    if step_mistakes == len(word):
                        mistakes += 1
            status_bar(word, result, mistakes)
        else:
            status_bar(word, result, mistakes)
            print("--------------------------------------")
            print("Correct! The right answer was " + word.upper())
            print(name + " You won!")
            print("--------------------------------------")
            print("\n")
            game(name)
    status_bar(word, result, mistakes)
    print("--------------------------------------")
    print("The right answer was " + word.upper())
    print(name + " You lost.. try one more time")
    print("--------------------------------------")
    print("\n")
    game(name)


def start_menu():
    """
    Start menu giving choice for user how to proceed
    """
    while True:
        print(MENU)
        choice = input("Enter Your choice:")
        ("\n")
        try:
            if not choice.isnumeric():
                raise ValueError("This is not a number")
            elif int(choice) > 3:
                raise ValueError("Entered value should be between 1 and 3")
            else:
                if int(choice) == 1:
                    print("\n")
                    print("Before we begin..")
                    player = input("...enter Your name:").upper()
                    game(player)
                elif int(choice) == 2:
                    print(INSTRUCTIONS)
                    start_menu()
                else:
                    break
        except ValueError as e:
            print(e)


def starting_window():
    """
    Function allowing to show the logo,
    just before game
    """
    print(WELCOME)
    start_menu()


starting_window()