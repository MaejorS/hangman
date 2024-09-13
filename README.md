# Halloween Hangman
Welcome to Halloween Hangman, a spooky version of the classic word-guessing game! In this game, the player has to guess the Halloween-themed word one letter at a time.

# Mockup Screenshots
Below is the single mockup of the main playing area of the game created using Placeit
<br>

![Project Screenshot](/images/mockupshangman.png)

<br>

# How to Play

- The computer selects a random word from the Halloween-themed word list.
- The player guesses one letter at a time.
- For every incorrect guess, the number of attempts decreases.
- The player either successfully guesses the word or loses when all attempts are used up.

# UX
The Halloween Hangman game is designed to be engaging and spooky while keeping a simple user interface. Players can guess letters and track their progress, seeing visual changes as incorrect guesses are stored in their own set and the correct guesses are revealed with each correct guess. They also get a fun Halloween ascii art whether they win or lose.

The design ensures that users can:

- Easily understand and play the game.
- View their remaining attempts and see the letters as they guess correctly.
- Get clear feedback for correct or incorrect guesses.

# Colour Scheme
The chosen color scheme for Hallooween Hangman is standard terminal color. This incluedes black background with white text.

# Typography
The game uses standard terminal font. 

# User Stories
- As a new user, I want to understand how to play the game so I can start guessing letters.
- As a new user, I want to see a visual representation of how many chances I have left, so I know how close I am to losing.
- As a returning user, I want to quickly restart the game after I win or lose so I can keep playing.
- As a new user, I want to enjoy a spooky Halloween theme as I play.

Returning Site Users
- As a returning user, I want to quickly restart the game to continue playing.
- As a returning user, I want to review the rules and scoring system to refresh my memory.

# Wireframes

Wireframes were developed for mobile, tablet and desktop. [Balsamiq](https://balsamiq.com/) was used to design the wireframes.
<br>

![Project Screenshot](/images/wireframehangman.jpg)

<br>

# Features
- A attempts left area so player can see how many guesses they have left before they lose.
<br>

![Project Screenshot](/images/feature-remain-guess.jpg)

<br>

- An attempted guesses area where the already guessed letters are stored in a set

<br>

![Project Screenshot](/images/feature-remain-guess.jpg)

<br>

- Win/lose ending that clears the terminal and lets the user know the word.

<br>

![Project Screenshot](/images/feature-end-game.jpg)

<br>


## Future Features
- A timer that adds an element of pressure and excitment for the player 
- A Goblin that appears as the player guesses wrong so that when they lose, a goblin gets them.
- A feature that allows the user to enter the full word at once in case they guess it early instead of one letter at a time.


# Testing


- Tested to make sure the score decreased as the player guessed wrong, that letters appeared as they were guessed correctly and that wrong guesses were stored in the set.
<br>

![Score Update](/images/testherokuscorekeep.jpg)

<br>
- Play again option appears in Heroku after player wins/loses.
<br>

![Play Again](/images/testherokuplayagain.jpg)

<br>

<br>
- Test user input to make sure they are prompted if incorret data is entered.
<br>

![Input test](/images/testduplicateguess.jpg)

<br>
- It is difficult to show text, but made sure terminal cleared after every guess. Timer allowed prompt to update user and let them know to wait before entering a new guess.

<br>

![Clear terminal](/images/testherokuterminalclear.jpg)

<br>

# Bugs and Fixes
- The biggest bug occured trying to get the terminal cleared. Part of the title kept sticking to the top of the terminal. Forgot to take a screen shot. Spent at least an hour troubleshooting and found out that the original function did not clear the terminal properly in Heroku. To fix, I had to research how else to clear the terminal using ANSI escape codes as outlined in the screenshots. Note, it all worked fine in gitpod. However, it did not work well with Heroku deployment. 

<br>

![Clear Terminal Bug Funciton](/images/bugclearterminal1.jpg)

<br>

<br>

![Clear Terminal Bug FIX](/images/bugfixclearterminal.jpg)

<br>

- The score was not updating properly, but realized the function was incomplete and the score was not updated properly

<br>

![Score bug](/images/bugscorenotupdating.jpg)

<br>

<br>

![Score bug fix](/images/bugfixupdatingset.jpg)

<br>

- Indentation error caused app not to run. Fixed with proper indentation.

<br>

![Indentation error](/images/indentationerror2.jpg)

# Validator Testing
## PEP 8
no errors were found when I put through the PEP 8 validator
<br>

![Project Screenshot](/images/cipep8validator.jpg)

# Deployment
The site was deployed using Code Institute's mock terminal for Heroku.

- Steps for deployment:
    - Fork or clone this repository.
    - Create a new Heroku app
    - Set the buildbacks to python and NodeJS in that order
    - Link the Heroku app to the repository
    - Click on Deploy


The live link can be found [here](https://megan-hangman-python-game-11990bf92930.herokuapp.com/).

# Credits
## Content
- Tutorial on clearing terminal [Coding with TJ](https://www.youtube.com/watch?v=LQzwMdplVw0)
## Media
- [Ascii art](https://www.asciiart.eu/holiday-and-events/halloween) ascii art

# Acknowledgments
- Thanks to my mentor [Chris Quinn](https://github.com/10xOXR) for planning and helpful feedback throughout the project.