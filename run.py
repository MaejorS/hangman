import random

WORD_LIST = ["magic", "manifestation", "cosmic", "destiny", "fate", "divine", "spirit", "abundance"]

def select_random_word(word_list):
    """
    Selects a random word from the provided word list.
    """
    return random.choice(word_list)

def display_word_progress(word, guessed_letters):
    """
    Displays the currenty progress of the word being guessed.
    Shows correct guesses and underscores for the remaining letters.
    """
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def get_user_guess():
    """
    Gets a letter guess from the user. Handles invalid input by prompting user again.
    """
    while True:
        guess = input("Enter a letter to guess: ").lower()
        if guess.isalpha() and len(guess) == 1: 
            return guess
        else:
            print("Please enter a single letter.")

def play_hangman():
    """
    Main function to play the game Hangman
    """

    # Pick the secret word
    word_to_guess = select_random_word(WORD_LIST)
    guessed_letters = set() # Letters user guesses correctly
    incorrect_guesses = set() # Letters user guesses incorrectly
    max_attempts = 5 # User gets 5 chances to guess before losing

    print("Let's Play Hangman :)")
    print("Instructions: You have 5 chances to guess the word correctly. Otherwise, you LOSE!")




# Run game
if __name__ == "__main__":
    play_hangman()