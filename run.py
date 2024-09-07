import random
import os
import time

WORD_LIST = ["magic", "manifestation", "cosmic", "destiny", "fate", "divine", "spirit", "abundance"]

def clear_terminal(): # Advised by mentor to add for polished look. Used Youtube tutorial to learn how to implement
    """
    Clears terminal after 3 or 4 lines based on user's operating system.
    """
    os.system('cls' if os.name == 'nt' else 'clear')

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

    

    # Ask guesses until game ends. This is the game loop
    while len(incorrect_guesses) < max_attempts:
        clear_terminal() # Clears terminal. Advised by mentor to add for polished look
        print("Let's Play Hangman :)")
        print("Instructions: You have 5 chances to guess the word correctly. Otherwise, you LOSE!")
        print(f"\nIncorrect guess: {', '.join(incorrect_guesses)}")
        print(f"Remaining attempts: {max_attempts - len(incorrect_guesses)}")
        print(f"\nWord to guess: {display_word_progress(word_to_guess, guessed_letters)}")

        # Ask player for guess
        guess = get_user_guess()

        # Check if guess is correct
        if guess in guessed_letters or guess in incorrect_guesses:
            print(f"\nYou already guessed that letter. Try another letter!")
            print(f"Please wait until this message clears to enter your next guess")
            time.sleep(1.5)
            continue

        if guess in word_to_guess:
            print(f"\nGood guess! '{guess}' is in the word :)")
            print(f"Please wait until this message clears to enter your next guess")
            guessed_letters.add(guess)
        else:
            print(f"\nSorry, '{guess}' is not in the word :(")
            print(f"Please wait until this message clears to enter your next guess")
            incorrect_guesses.add(guess)
        
        time.sleep(1.5)

            

        # Check if player guessed the word
        if all(letter in guessed_letters for letter in word_to_guess):
            word_progress = display_word_progress(word_to_guess, guessed_letters)
            clear_terminal()
            print(f"Happy Days! You've guessed the word: {word_to_guess}")
            break
    else:
        clear_terminal()
        print(f"\nSad Day! You've run out of chances! The word was: {word_to_guess}")
    
    print("Thank you for playing Hangman :)")

# Check if player wants to play again
def play_again():
    """
    Asks player if they want to play again.
    """
    while True:
        choice = input("Wanna go again? (yes/no): ").lower()
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
        
