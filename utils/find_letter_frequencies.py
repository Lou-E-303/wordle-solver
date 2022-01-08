from collections import Counter
from utils.valid_answers import get_valid_answers


def find_letter_frequencies():

    five_letter_words = get_valid_answers()

    letter_frequencies = Counter(''.join(five_letter_words))

    letter_frequencies_most_common = dict(letter_frequencies.most_common())

    return letter_frequencies_most_common

    # A, E, S, O, R are the most common letters
    # Therefore by this metric 'arose' should be our starting word
