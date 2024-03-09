import random
words_to_guess = ['''
Cucamber''', '''Pinapple''', '''Banana''', '''
Melon''', '''Papaya''', '''Mango''', '''
Carrot''', '''Potatoe''', '''Orange''', '''
Pear''', '''Tomatoe''', '''Cabage''', '''
Onion''']

guessed_letters = []
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

S_MENU = '''

What do You want to do next?
Press "1" to start new game
Press "2" to quit

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


def players_name():
    """
    Get players name, limiting that only letters can be entered
    and num of symbols should be between 2 and 12
    """
    while True:
        try:
            player = input("...enter Your name:\n").upper()
            if player.isalpha() is False:
                raise ValueError("Only latin letters are allowed!")
            elif len(player) <= 2 or len(player) >= 12:
                raise ValueError("Sign limit! Use 2 to 12 signs")
            else:
                return player
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
    print("You have still " + str(len(HANGMANPICS) - score - 1) + " lives!")
    print("--------------------------------------")
    print("\n")


def game(name):
    """
    Clears the list of previosly guessed letters
    Gets from user word, replaces it with hidden word,
    Guess by guess counts the mistakes of the user.
    Updates the result and gets it back.
    """
    del guessed_letters[:]
    word = get_words(words_to_guess)
    secret = hidden_word(word)
    print("\n")
    print(name + " I hope You are ready! Let's start!")
    print(secret)
    print("Word, You have to guess has " + str(len(secret)) + " letters!")
    print("\n")
    mistakes = 0
    print(HANGMANPICS[mistakes])
    print("\n")
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
            end_menu(name)
    status_bar(word, result, mistakes)
    print("--------------------------------------")
    print("The right answer was " + word.upper())
    print(name + " You lost.. try one more time")
    print("--------------------------------------")
    print("\n")
    end_menu(name)


def start_menu():
    """
    Start menu giving choice for user how to proceed
    """
    print(MENU)
    while True:
        choice = input("Enter Your choice:")
        ("\n")
        try:
            if not choice.isnumeric():
                raise ValueError("This is not a number")
            elif int(choice) < 1 or int(choice) > 3:
                raise ValueError("Entered value should be between 1 and 3")
            else:
                if int(choice) == 1:
                    print("\n")
                    print("Before we begin..")
                    player = players_name()
                    game(player)
                elif int(choice) == 2:
                    print(INSTRUCTIONS)
                    start_menu()
                break
        except ValueError as e:
            print(e)


def end_menu(name):
    """
    Menu when a game is finished, so used can decide what to do next
    """
    print(S_MENU)
    while True:
        choice = input("Enter Your choice: \n")
        ("\n")
        try:
            if not choice.isnumeric():
                raise ValueError("This is not a number")
            elif int(choice) < 1 or int(choice) > 3:
                raise ValueError("Entered value should be between 1 or 2")
            else:
                if int(choice) == 1:
                    game(name)
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
