# Halloween Hangman
Welcome to Halloween Hangman, a spooky version of the classic word-guessing game! In this game, the player has to guess the Halloween-themed word one letter at a time.

# Mockup Screenshots
Below is the single mockup of the main playing area of the game created using Placeit
<br>

![Project Screenshot](/assets/images/mockuprpsls.png)

<br>

# How to Play

- The computer selects a random word from the Halloween-themed word list.
- The player guesses one letter at a time.
- For every incorrect guess, the Grim Reaper slowly disappears, and the number of attempts decreases.
- The player either successfully guesses the word or loses when all attempts are used up.

# UX
The Halloween Hangman game is designed to be engaging and spooky while keeping a simple user interface. Players can guess letters and track their progress, seeing visual changes as incorrect guesses result in the Grim Reaper disappearing piece by piece.

The design ensures that users can:

- Easily understand and play the game.
- View their remaining attempts and the Grim Reaper figure as it disappears.
- Get clear feedback for correct or incorrect guesses.

# Colour Scheme
The chosen color scheme for Hallooween Hangman is standard terminal color. This incluedes black background with white text.

# Typography
The game uses the Google Font called 'Asap' for its modern and clean style. This font was chosen for its readability and compatibility with the game's aesthetic.

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

- 
## Future Features
- A timer that adds an element of pressure and excitment for the player 
- A Goblin that appears as the player guesses wrong so that when they lose, a goblin gets them.
- A feature that allows the user to enter the full word at once in case they guess it early instead of one letter at a time.


# Testing

- Firefox, Chrome and Safari were used to test the game in the Heroku app.
- Scores increment properly, game over function works and play feature clears terminal and starts game over.
- 
<br>

![Project Screenshot]()

<br>
- I tested to make sure that icons change color depending on whether user wins or loses to the computer.
<br>

![Project Screenshot]()

<br>

![Project Screenshot]()

<br>
- 
- 

<br>

![Project Screenshot]()

<br>

- Used [WAVE](https://wave.webaim.org/) web accessability evaluation tool to check for accessability issues. A couple of minore notes about an h2 tag and the justified text

![Project Screenshot](/assets/images/wavetest.jpg)

# Bugs and Fixes
- 

<br>

![Project Screenshot](/assets/images/invalidassignment.jpg)

<br>

- when trying to display increase in score in the game and display in the span, it was not displaying the increase as a result of the error below. forgot to call .innerHTML in win function under computerScore_span. Once corrected, it started increasing the score as expected.

<br>

![Project Screenshot](/assets/images/userscorespannotdefined.jpg)

<br>

- when updating win function to get result_div, css styles were removed from div as shown below. When I got the reference from the element document.querySelector(".result"), I forgot that the text is stored in a p element. Incluced p tag to correct error.

<br>

![Project Screenshot](/assets/images/divadjust.jpg)

# Validator Testing
## PEP 8
no errors were found when I put through the PEP 8 validator
<br>

![Project Screenshot]()

# Deployment
The site was deployed to GitHub Pages. The steps to deploy are as follows:


The live link can be found [here]().

# Credits
## Content
- Tutorial on clearing terminal [Tutorial Name]()
## Media
- [Ascii art]() ascii art

# Acknowledgments
- Thanks to my mentor [Chris Quinn](https://github.com/10xOXR) for planning and helpful feedback throughout the project.