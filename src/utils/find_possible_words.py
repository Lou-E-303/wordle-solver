from src.utils.valid_answers import get_valid_answers


# Find all the words that fit the following criteria:
# 1. They have not been guessed before ✅
# 2. They have the green letters in the correct indices ✅
# 3. They have the yellow letters in them somewhere (but not at the same index as previous guess) ✅
# 4. They haven't got the grey letters in them anywhere, unless the grey letter is also an unresolved yellow ✅
# 5. They haven't got more of the same letters than unresolved yellows if there is a grey of that letter ✅
# 6. They haven't got green or yellow letters in indices which have failed before ✅


def find_possible_words(guess, yellow_letters, grey_letters, green_letters, previous_guesses):
    possible_words = get_valid_answers()

    def is_word_possible(word):
        return (word not in previous_guesses and
                green_letters_correct(guess, word) and
                yellow_letters_correct(yellow_letters, word) and
                grey_letters_correct(grey_letters, yellow_letters, green_letters, word))

    return filter(is_word_possible, possible_words)


def green_letters_correct(guess, possible_word):
    for i in range(len(possible_word)):
        if possible_word[i] != guess[i] and guess[i] != '*':
            return False
    return True


def yellow_letters_correct(yellow_letters, possible_word):
    for index, letter in yellow_letters.items():
        if possible_word[index] == letter:
            return False
        if letter not in possible_word:
            return False
    return True


def grey_letters_correct(grey_letters, yellow_letters, green_letters, possible_word):
    grey_letter_values = [item for sublist in list(grey_letters.values()) for item in sublist]

    for i, letter in enumerate(possible_word):

        if letter in yellow_letters.values() and letter in grey_letter_values:
            yellow_letter_maximum = list(yellow_letters.values()).count(letter)
            yellow_letter_count = list(possible_word).count(letter)
            if yellow_letter_count > yellow_letter_maximum:
                return False

        if letter in green_letters or letter in yellow_letters.values():
            if i in grey_letters:
                if letter in grey_letters[i]:
                    return False
        else:
            if any(letter in val for val in grey_letters.values()):
                return False

    return True
