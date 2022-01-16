from utils.valid_answers import get_valid_answers


# Find all the words that fit the following criteria:
# 1. They have not been guessed before ✅
# 2. They have the green letters in the correct indices ✅
# 3. They have the yellow letters in them somewhere (but not at the same index as previous guess) ✅
# 4. They haven't got the grey letters in them anywhere ✅
# 5. They haven't got green or yellow letters in indices which have failed before ✅


def find_possible_words(guess, yellow_letters, grey_letters, green_letters, previous_guesses):
    possible_words = get_valid_answers()

    for possible_word in possible_words.copy():
        if possible_word in previous_guesses:
            possible_words.remove(possible_word)

        elif not green_letters_correct(guess, possible_word):
            possible_words.remove(possible_word)

        elif not yellow_letters_correct(yellow_letters, possible_word):
            possible_words.remove(possible_word)

        elif not grey_letters_correct(grey_letters, yellow_letters, green_letters, possible_word):
            possible_words.remove(possible_word)

    return possible_words


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
    for i, letter in enumerate(possible_word):
        if letter in green_letters or letter in yellow_letters.values():
            if i in grey_letters:
                if letter in grey_letters[i]:
                    return False
        else:
            if any(letter in val for val in grey_letters.values()):
                return False

    return True
