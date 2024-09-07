import random

WORD_LIST = ["magic", "manifestation", "cosmic", "destiny", "fate", "divine", "spirit", "abundance"]

def select_random_word(word_list)
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
