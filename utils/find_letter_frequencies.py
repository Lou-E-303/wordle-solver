from collections import Counter
from utils.load_all_words import load_all_words


def find_letter_frequencies():

    five_letter_words = load_all_words('resources/five_letter_words_one_line.txt')

    letter_frequencies = Counter(str(five_letter_words))

    letter_frequencies.pop('\'')
    letter_frequencies.pop('{')
    letter_frequencies.pop('}')

    letter_frequencies_most_common = dict(letter_frequencies.most_common())

    return letter_frequencies_most_common

    # A, E, S, O, R are the most common letters
    # Therefore by this metric 'arose' should be our starting word
