# HANGMAN game

Hangman game is a simple game where a user has to guess a word letter by letter.
Word is taken from a prepared list of words.
User has to guess the word, before the man is hanged.

[HANGMAN Game](https://vegetable-hangman-ba3fa81e72d4.herokuapp.com/)

![Design is responsive](/assets/images/mockup.JPG)

## How to play

Hangman is based on globaly well known game "Hangman", just in this case user is playing it against computer. Cumputer is randomly picking one word from the list. It is displayed to user how many symbols the word has.
User will guess letter by letter, each rigth answered letter will be displayed in hidden word, but for each wrong answer, 1 line will be added to the man hanging on the hangers.
Game finished, when the man is hanged or the word is answered.

## Flowchart

![Process fowchart](/assets/images/flowchart.jpg)

## Features

### Existing features

* Welcome message and start menu
    * Game logo is displayed on the top
    * Starting menu is offered to user - to start game, quit game or read instructions
![Start screen](/assets/images/features/startscr.JPG)

* Instructions
    * Displayed short game instructions to customer
    * Below the instructions - main menu is displayed for further possible navigation
![Navigation](/assets/images/features/instructions.JPG)

* Players name entery
    * to make more personal approach afterwards, user is asked to enter name
![username](/assets/images/features/username.JPG)

* Start game status
    * A welcome message is displayed to player
    * The hidden word is showed - letters are replaced with *
    * In text there is written, how many letters player has to guess.
    * "Empty" hangers are displayed
    * User is asked to enter first letter
![First game screen](/assets/images/features/first_game_screen.JPG)


### Furure features

* add additional words in list
* add a possiblity for user to choose words from few lists by criteria as topic
* players statistics - winned and lost games