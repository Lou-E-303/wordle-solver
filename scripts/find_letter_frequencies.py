from load_words import load_words
from collections import Counter

five_letter_words = load_words('../resources/five_letter_words_one_line.txt')

letter_frequencies = Counter(str(five_letter_words))

letter_frequencies.pop('\\')
letter_frequencies.pop('\'')
letter_frequencies.pop('\"')
letter_frequencies.pop('{')
letter_frequencies.pop('}')
letter_frequencies.pop('/')

# A, E, S, O, R are the most common letters
# Therefore by this metric 'arose' should be our starting word
