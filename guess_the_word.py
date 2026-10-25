# Jordan Fenn
# CIS256 Fall 2026
# Programming Assignment 4

import random

# Words the game can choose from. Every secret word comes from this list.
WORD_LIST = ["python", "college", "function", "variable", "loop", "koala"]


def choose_word(words=None):
    """Pick one secret word at random from the predefined list."""
    # Default to the module list so callers and tests can pass another list.
    if words is None:
        words = WORD_LIST
    return random.choice(words)


# How many wrong letters the player may guess before the game ends.
MAX_ATTEMPTS = 6


def mask_word(word):
    """Hide every letter so the player starts with a blank for each character."""
    return ["_"] * len(word)


def apply_guess(word, mask, guess, attempts_left, guessed):
    """Apply one letter guess to the current mask.

    A correct letter is written into every matching blank. A wrong letter
    costs one attempt. Repeats and non-letters do not cost an attempt.
    The mask and guessed set are updated in place. The attempts still left
    and a status string are returned because an int cannot be updated in place.
    """
    # Compare letters without caring about capitalization or extra spaces.
    letter = guess.strip().lower()

    if len(letter) != 1 or not letter.isalpha():
        return attempts_left, "invalid"

    if letter in guessed:
        return attempts_left, "repeat"

    guessed.add(letter)

    if letter in word:
        # Reveal every copy of the letter, not only the first one.
        for index, character in enumerate(word):
            if character == letter:
                mask[index] = letter
        return attempts_left, "correct"

    return attempts_left - 1, "incorrect"
