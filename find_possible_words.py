from scripts.load_words import load_words

# Find all the words that fit the following criteria:
# 1. They have not been guessed before ✅
# 2. They have the green letters in the correct indices ✅
# 3. They have the yellow letters in them somewhere (but not at the same index as previous guess) ✅


def find_possible_words(guess, yellow_letters, previous_guesses):
    possible_words = load_words('resources/five_letter_words.txt')

    for word in possible_words.copy():
        if word in previous_guesses:
            possible_words.remove(word)
        elif not green_letters_correct(guess, word):
            possible_words.remove(word)
        elif not yellow_letters_correct(yellow_letters, word):
            possible_words.remove(word)

    print(possible_words)
    return possible_words


def green_letters_correct(guess, word):
    for i in range(len(word)):
        if word[i] != guess[i] and guess[i] != '*':
            return False
    return True


def yellow_letters_correct(yellow_letters, word):
    for index, letter in yellow_letters.items():
        if word[index] == letter:
            return False
        if letter not in word:
            return False
    return True
