from utils.find_letter_frequencies import find_letter_frequencies


def suggest_next_guess(possible_words):
    letter_frequencies = find_letter_frequencies()

    word_score_pairs = {}

    for word in possible_words:
        score = 0

        for letter in word:
            score = score + letter_frequencies[letter]
        word_score_pairs[word] = score

    suggested_guesses = sorted(word_score_pairs.items(), key=lambda x: x[1], reverse=True)

    return suggested_guesses


