import random


def get_word(wordfile="/usr/share/dict/words"):
    good_words = []
    with open(wordfile) as f:
        for i in f:
            i = i.strip()
            if i.isalpha() and i.islower() and len(i) >= 5:
                good_words.append(i)
    return random.choice(good_words)


def mask_word(secret_word, guesses):
    op = []
    for i in secret_word:
        if i in guesses:
            op.append(i)
        else:
            op.append("-")
    return "".join(op)


def hangman_create_status(secret_words, guesses, remaining_turn):
    masked_word = mask_word(secret_words, guesses)
    guessed = " ".join(guesses)
    return f"""
    Word:{masked_word}
    Guesses:{guessed}
    Remaining_turns:{remaining_turn}
    """
