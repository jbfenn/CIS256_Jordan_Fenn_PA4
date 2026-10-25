# Jordan Fenn
# CIS256 Fall 2026
# Programming Assignment 4

import guess_the_word


def test_selected_word_comes_from_predefined_list():
    """The word the game selects must be one of the words in WORD_LIST."""
    # Call it more than once because choose_word picks at random.
    for _ in range(20):
        selected = guess_the_word.choose_word()
        assert selected in guess_the_word.WORD_LIST


def test_correct_guess_reveals_every_matching_letter():
    """A correct letter fills every matching position and keeps the attempt count."""
    word = "banana"
    mask = guess_the_word.mask_word(word)
    guessed = set()

    attempts_left, status = guess_the_word.apply_guess(
        word, mask, "a", 6, guessed
    )

    assert status == "correct"
    assert mask == ["_", "a", "_", "a", "_", "a"]
    assert attempts_left == 6


def test_incorrect_guess_costs_one_attempt():
    """A letter that is not in the word leaves the mask blank and uses an attempt."""
    word = "python"
    mask = guess_the_word.mask_word(word)
    guessed = set()

    attempts_left, status = guess_the_word.apply_guess(
        word, mask, "z", 6, guessed
    )

    assert status == "incorrect"
    assert mask == ["_"] * len(word)
    assert attempts_left == 5
