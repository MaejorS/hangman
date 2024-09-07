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

    # Ask guesses until game ends. This is the game loop
    while len(incorrect_guesses) < max_attempts:
        print(f"\nWord to guess: {display_word_progress(word_to_guess, guessed_letters)}")
        print(f"Incorrect guess: {', '.join(incorrect_guesses)}")
        print(f"Remaining attempts: {max_attempts - len(incorrect_guesses)}")

        # Ask player for guess
        guess = get_user_guess()

        # Check if guess is correct
        if guess in guessed_letters or guess in incorrect_guesses:
            print("You already guessed that letter. Try another letter!")
            continue

        if guess in word_to_guess:
            print(f"Good guess! '{guess}' is in the word :)")
            guessed_letters.add(guess)
        else:
            print(f"Sorry, '{guess}' is not in the word :(")

# Run game
if __name__ == "__main__":
    play_hangman()