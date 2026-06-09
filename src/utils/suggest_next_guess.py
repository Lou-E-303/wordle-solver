import sys

def suggest_next_guess(possible_words, letter_frequencies, current_round):
    word_score_pairs = {}
    duplicate_letter_penalty = 750 - (current_round * 150)

    if len(possible_words) == 1:
        return possible_words[0]

    for word in possible_words:
        score = 0
        letters_in_word = {}

        for letter in word:
            if letter not in letters_in_word:
                letters_in_word[letter] = 1
            else:
                letters_in_word[letter] += 1
                print("duplicate letter: " + letter + " found in word " + word + ", applying penalty of " + str(duplicate_letter_penalty))
                score -= duplicate_letter_penalty

            score = score + letter_frequencies[letter]

        word_score_pairs[word] = score

    suggested_guesses = sorted(word_score_pairs.items(), key=lambda x: x[1], reverse=True)

    if len(suggested_guesses) == 0:
        print("No possible words found - this may be a fault of the dictionary this solver uses (sorry!), or you may not have entered the results correctly.")
        sys.exit(0)

    for word, score in suggested_guesses:
        print("Word: " + word + " Score: " + str(score))

    return suggested_guesses[0][0]


