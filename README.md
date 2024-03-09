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

* Next letter guessing
    * Hidden word is updated with right answered letters
    * Updated status of hangers is displayed
    * List of already guessed letters, is displayed
    * Information, how many tries player has left is indicated on the screen

![Next guess screen](/assets/images/features/next_guess.JPG)

* Winners screen
    * Message that game has been won.
    * Confirming, what was the right word
    * Below is displayed small menu for further navigation

![Winners screen](/assets/images/features/win_screen.JPG)

* Lost game screen
    * Hanging man is showed
    * User sees that no lives has left
    * Personal (with players name) message is displayed to inform that game is lost

![Lost game screen](/assets/images/features/lost_game.JPG)

* Small menu
    * After won or lost game small menue is given for user to choose - play another game or quit

![Small menu](/assets/images/features/small_menu.JPG)

* Input validation in menu´s
    * User input is validated, to be sure that user can not enter number too small, too big or to input other symbol 

![Input validation in menu](/assets/images/features/valid_exampl_num.JPG)

* Letter input validation
    * User input is validated, to be sure that user can not enter number, or string that would be too long 

![Letter input validation](/assets/images/features/letter_entery.JPG)

* Players name validation
    * User input is validated with limit of 2 - 12 symbols. And no numbers are allowed

![Players name validation](/assets/images/features/username_validation.JPG)

### Future features

* add additional words in list
* add a possiblity for user to choose words from few lists by criteria as topic
* players statistics - winned and lost games

## Technologies used

* Python

## Frameworks, Libraries & Programs Used

* [Gitpod](https://www.gitpod.io/) for writing final code
* [GitHub](https://github.com/) for storage of app
* [Trinket](https://trinket.io/) for quick tests of code
* [Python tutor](https://pythontutor.com/) for visual debugging
* [Figma](https://www.figma.com/) for drawing flowchart
* [Am I responsive](https://ui.dev/amiresponsive) used for the mockup picture of readme file
* [CI Python Linter](https://pep8ci.herokuapp.com/#) used for code validation
* [ASCII Art Generator](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20) to create welcome message

## Testing

### Validation testing

For data validation was used [CI Python Linter](https://pep8ci.herokuapp.com/#). All the indicated errors were corrected.

![No errors](/assets/images/no_errors.JPG)

### Manual testing

| Step | Input | Expected result | Received | Completed? |
| ---- | ----- | --------------- | -------- | ------ |
| Start screen | no | Showed logo | Showed logo | Yes |
| Start screen | no | Menu loaded | Menu loaded | Yes |
| Start menu | " " | This is not a number | This is not a number | Yes |
| Start menu | empty | This is not a number | This is not a number | Yes |
| Start menu | a | This is not a number | This is not a number | Yes |
| Start menu | 1234 | Entered value should be between 1 and 3 | Entered value should be between 1 and 3 | Yes |
| Start menu | 0 | Entered value should be between 1 and 3 | Entered value should be between 1 and 3 | Yes |
| Start menu | 3 | Game quited | Game quited | Yes |
| Start menu | 2 | Instructions loaded | Instructions loaded | Yes |
| Start menu | 1 | Game loaded | Game loaded | Yes |
| Instructions menu | 3 | Game quited | Game quited | Yes |
| Instructions menu | 1 | Game loaded | Game loaded | Yes |
| Game | no | load request of name at beginning | load request of name at beginning | Yes |
| Name entery | 1 | Only latin letters are allowed! | Only latin letters are allowed! | Yes |
| Name entery | 0 | Only latin letters are allowed! | Only latin letters are allowed! | Yes |
| Name entery | a | Sign limit! Use 2 to 12 signs | Sign limit! Use 2 to 12 signs | Yes |
| Name entery | Alexander the Great | Only latin letters are allowed! | Only latin letters are allowed! | Yes |
| Name entery | Janis | result accepted, moved to next step | result accepted, moved to next step | Yes |
| Game first step | no | Load welcome letter with players name | Load welcome letter with players name | Yes |
| Game first step | no | Load hidden word - letters replaced with * | Load hidden word - letters replaced with * | Yes |
| Game first step | no | Show to user the number of hidden letters | Show to user the number of hidden letters | Yes |
| Game first step | no | Show first hangman from list | Show first hangman from list | Yes |
| Game first step | no | Ask for letter entery | Ask for letter entery | Yes |
| Letter entery | 1 | Only latin letters are allowed! | Only latin letters are allowed! | Yes |
| Letter entery | as | You must enter only one symbol! | You must enter only one symbol! | Yes |
| Letter entery | a | move to next step | move to next step | Yes |
| Status bar | no | show current result - hidden word with unhiden already answered letters. (Entered letter A) | show current result - hidden word with unhiden already answered letters(Entered letter A - and it was replaced in the list of *) | Yes |
| Status bar | no | show hanged man status | show hanged man status | Yes |
| Status bar | no | show already guessed letters | Letters You have guessed till now ['A'] | Yes |
| Status bar | no | show how many tries are left | You have still 6 lives | Yes |
| Repeated entery of same letter | a | you have already used this letter for guess | you have already used this letter for guess | Yes |
| Repeated entery of same letter.upper() | A | you have already used this letter for guess | you have already used this letter for guess | Yes |
| Lost game | no | load players current result - word with unhidden guessed letters | load players current result - word with unhidden guessed letters | Yes |
| Lost game | no | hanged man "image" | hanged man "image" | Yes |

| Lost game | no | hanged man "image" | hanged man "image" | Yes |

| Lost game | no | show "The right answer was" + word | show "The right answer was PINAPPLE | Yes |
| Lost game | no | show small menu | show small menu | Yes |
| Small menu | a | This is not a number | This is not a number | Yes |
| Small menu | 0 | Entered value should be between 1 and 2 | Entered value should be between 1 and 2 | Yes |
| Small menu | 15 | Entered value should be between 1 and 2 | Entered value should be between 1 and 2 | Yes |
| Small menu | 1 | restart the game | restart the game | Yes |
| Small menu | 2 | quit the game | quit the game | Yes |
| Win game | no | congatulation message with players name | congatulation message with players name | Yes |
| Win game | no | congatulation message with players name | congatulation message with players name | Yes |
| Win game | no | show small menu | show small menu | Yes |

## Credits

* Mentor Mitko Bachvarov
    * support for generating ideas to fulfill project
    * support for problem solving
    * encourage and motivation!

### Code

* [Python essentials template](https://github.com/Code-Institute-Org/python-essentials-template) by [Code insitute](https://codeinstitute.net/global/) 
* Slack comunity
* Code insitute lecture materials
* [w3schools](https://www.w3schools.com/) for repeating clarafication for some functions
* [Python documentation](https://docs.python.org/3/tutorial/errors.html) for understanding in detail "Errors and Exceptions"
* [Programiz](https://www.programiz.com/) for explaining .isnumeric() and .isalpha() methods
* [Stackowerflow](https://stackoverflow.com/) for readme file table formating

