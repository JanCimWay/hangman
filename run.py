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
    print(word)
    print(result)
    print(guessed_letters)
    print(HANGMANPICS[score])
    print("You have made " + str(score) + " mistakes till now!")
    print("\n")

def get_welcome_msg():
    print("welcome")

def game():
    """
    Clears the list of previosly guessed letters
    Gets from user word, repalces it with hidden word, 
    Guess by guess counts the mistakes of the user.
    Updates the resul and gets it back.
    """
    print("\n")
    del guessed_letters[:]
    get_welcome_msg()
    print("\n")
    word = get_words(words_to_guess)
    secret = hidden_word(word)
    guess = guess_letter()
    result = replace_letter(secret, word, guess)
    mistakes = 0
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
          print(word)
          print("You won!")
          print("\n")
          game()
    print("You lost.. try one more time")
    print(word)
    print("\n")
    game()

def start_menu():
  while True:
    print(MENU)
    choice = input("Enter Your choice:")
    ("\n")
    try:
        if not choice.isnumeric():
            raise ValueError("This is not a number")
        elif int(choice) > 3:
            raise ValueError("Your chosen Value is too big! You should choose number between 1 and 3")
        else:
            if int(choice) == 1:
                game()
            elif int(choice) == 2:
                print(INSTRUCTIONS)
                start_menu()
            else:
                break
    except ValueError as e:
      print(e)

start_menu()