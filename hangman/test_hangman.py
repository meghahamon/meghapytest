import os

import hangman


def test_get_word_no_punctuation():
    with open("/tmp/words.txt", "w") as f:
        f.write("elephant\n")
        f.write("car's\n")
        f.write("planes's\n")
        f.write("amazing!!!\n")
    for _ in range(100):
        word = hangman.get_word("/tmp/words.txt")
        assert word == "elephant"
    os.unlink("/tmp/words.txt")


def test_get_word_no_proper_nouns():
    with open("/tmp/words.txt", "w") as f:
        f.write("elephant\n")
        f.write("Noufal\n")
        f.write("John\n")
        f.write("Simon\n")
    for _ in range(100):
        word = hangman.get_word("/tmp/words.txt")
        assert word == "elephant"
    os.unlink("/tmp/words.txt")


def test_get_word_min_length():
    with open("/tmp/words.txt", "w") as f:
        f.write("elephant\n")
        f.write("egg\n")
        f.write("an\n")
        f.write("fun\n")
    for _ in range(100):
        word = hangman.get_word("/tmp/words.txt")
        assert word == "elephant"
    os.unlink("/tmp/words.txt")


def test_mask_word_single_letter():
    secret_word = "elephant"
    guesses = ["l"]
    ret = hangman.mask_word(secret_word, guesses)
    assert ret == "-l------"


def test_mask_word_multiple_letters():
    secret_word = "elephant"
    guesses = ["e"]
    ret = hangman.mask_word(secret_word, guesses)
    assert ret == "e-e-----"


def test_mask_word_mixed_letters():
    secret_word = "elephant"
    guesses = ["e", "a", "x", "p"]
    ret = hangman.mask_word(secret_word, guesses)
    assert ret == "e-ep-a--"


def test_create_status_no_guesses():
    secret_word = "elephant"
    guesses = []
    remaining_turn = 8
    ret = hangman.hangman_create_status(secret_word, guesses, remaining_turn)
    assert ret == """
    Word:--------
    Guesses:
    Remaining_turns:8
    """
