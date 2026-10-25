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
