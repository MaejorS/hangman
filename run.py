"""
Hangman Game Module.

This module implements the classic Hangman game where the player guesses
letters to figure out a secret word. It includes features such as selecting
a random word from a predefined list, displaying the current progress of
the word with correctly guessed letters, tracking correct and incorrect
guesses, limiting the number of incorrect guesses before the game ends,
and providing options to play the game again.

Functions:
- select_random_word(word_list): Picks a random word from the list.
- display_word_progress(word, guessed_letters): Shows the word with
  underscores for unguessed letters.
- get_user_guess(): Prompts the user to enter a single letter and validates
  the input.
- play_hangman(): Runs the main Hangman game loop.
- play_again(): Asks if the player wants to play another round.

Dependencies:
- random: For selecting a random word.
- os: For clearing the terminal screen.
- time: For adding delays between messages.
"""

import random
import os
import time

WORD_LIST = ["magic", "cemetery", "goblin", "potion",
             "bewitched", "spooky", "vampire", "pumpkin"]


def clear_terminal():  # Used Youtube tutorial to learn how to implement
    """Clear terminal after 3 or 4 lines based on user's operating system."""
    os.system('cls' if os.name == 'nt' else 'clear')


def select_random_word(word_list):
    """Select a random word from the provided word list."""
    return random.choice(word_list)


def display_word_progress(word, guessed_letters):
    """
    Display the current progress of the word being guessed.

    Show correct guesses and underscores for the remaining letters.
    """
    return " ".join([letter if letter in guessed_letters
                     else "_" for letter in word])


def get_user_guess():
    """Get a letter guess from the user. Prompt user if input is invalid."""
    while True:
        guess = input("Enter a letter to guess: ").lower()
        if guess.isalpha() and len(guess) == 1:
            return guess
        else:
            print("Please enter a single letter.")


def play_hangman():
    """Play the game Hangman."""
    # Pick the secret word
    word_to_guess = select_random_word(WORD_LIST)
    guessed_letters = set()  # Letters user guesses correctly
    incorrect_guesses = set()  # Letters user guesses incorrectly
    max_attempts = 5  # User gets 5 chances to guess before losing

    # Ask guesses until game ends. This is the game loop
    while len(incorrect_guesses) < max_attempts:
        #clear_terminal()  # Clears terminal after iteration
        print("""
 _   _       _ _                               
| | | | __ _| | | _____      _____  ___ _ __   
| |_| |/ _` | | |/ _ \ \ /\ / / _ \/ _ \ '_ \  
|  _  | (_| | | | (_) \ V  V /  __/  __/ | | | 
|_| |_|\__,_|_|_|\___/ \_/\_/ \___|\___|_| |_| 
| | | | __ _ _ __   __ _ _ __ ___   __ _ _ __  
| |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
|  _  | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                   |___/
              """
             )
        print("INSTRUCTIONS:")
        print("You have 5 chances.")
        print("Guess the Halloween-themed word correctly!")
        print("Otherwise, you LOSE!")
        print(f"\nIncorrect guess: {', '.join(incorrect_guesses)}")
        print(f"Remaining Guesses: {max_attempts - len(incorrect_guesses)}")
        print(
            "\nGuess the word: "
            f"{display_word_progress(word_to_guess, guessed_letters)}"
        )

        # Ask player for guess
        guess = get_user_guess()

        # Check if guess is correct
        if guess in guessed_letters or guess in incorrect_guesses:
            print("\nYou already used this letter. Try again!")
            print("Please wait to enter your next guess")
            time.sleep(2)
            continue

        if guess in word_to_guess:
            print(f"\nHOORAY! '{guess}' is in the word :)")
            print("Please wait to enter your next guess")
            guessed_letters.add(guess)
        else:
            print(f"\nNOPE, '{guess}' is not in the word :(")
            print("Please wait to enter your next guess")
            incorrect_guesses.add(guess)

        time.sleep(2)

        # Check if player guessed the word
        if all(letter in guessed_letters for letter in word_to_guess):
            clear_terminal()
            print(f"Happy Days! You've guessed the word: {word_to_guess}")
            break
    else:
        clear_terminal()
        print("\nSad Day! You've run out of chances!")
        print(f"The word was: {word_to_guess}")

        print("\nThanks for playing! Happy Halloween :)")
        print("""
      __       *                  ((((
*            *        *  (((
       *                (((      *
  *   / \        *     *(((
   __/___\__  *          (((
     (O)  |         *     ((((
*  '<   ? |__ ... .. .             *
     \@      \    *    ... . . . *
     //__     \\
    // ||\__   \    |~~~~~~ . . .   *
====M===M===| |=====|~~~~~~   . . .. .. .
         *  \ \ \   |~~~~~~    *
  *         <__|_|   ~~~~~~ .   .     ... .
           """
             )


# Check if player wants to play again
def play_again():
    """Ask player if they want to play again."""
    while True:
        choice = input("\nWanna go again? (yes/no): ").lower()
        if choice in {"yes", "y"}:
            return True
        elif choice in {"no", "n"}:
            return False
        else:
            print("Please enter 'yes' or 'no'.")


# Run game
if __name__ == "__main__":
    while True:
        play_hangman()
        if not play_again():
            print("See ya! At least you tried!")
            break
