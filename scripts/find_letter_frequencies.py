from load_words import load_words
from collections import Counter
import json

five_letter_words = load_words('resources/five_letter_words_one_line.txt')

letter_frequencies = Counter(str(five_letter_words))

letter_frequencies.pop('\\')
letter_frequencies.pop('\'')
letter_frequencies.pop('\"')
letter_frequencies.pop('{')
letter_frequencies.pop('}')
letter_frequencies.pop('/')

letter_frequencies = letter_frequencies.most_common()

with open('resources/letter_frequencies.json', 'w') as letter_frequencies_json:
    json.dump(dict(letter_frequencies), letter_frequencies_json)

print(letter_frequencies)

# A, E, S, O, R are the most common letters
# Therefore by this metric 'arose' should be our starting word
