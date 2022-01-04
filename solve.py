from scripts.load_words import load_words


def find_possible_words(guess, yellow_letters):
    possible_words = load_words('resources/five_letter_words.txt')

    for word in possible_words.copy():
        if word in previous_guesses:
            possible_words.remove(word)
        elif not green_letters_present(guess, word):
            possible_words.remove(word)
        elif not yellow_letters_present(yellow_letters, word):
            possible_words.remove(word)

    print(possible_words)
    return possible_words


def green_letters_present(guess, word):
    print("Word: " + word)
    for i in range(len(word)):
        print("i: ", i)
        print("word[i]: " + word[i] + " guess[i]: " + guess[i])
        if word[i] != guess[i] and guess[i] != '*':
            print("Returning False!")
            return False
    return True


def yellow_letters_present(yellow_letters, word):
    for index, letter in yellow_letters.items():
        if word[index] == letter:
            print("Word " + word + " contains letter " + letter + " at same index as previous guess - returning False!")
            return False
        if letter not in word:
            print("Letter " + letter + " not found in word " + word + " - returning False!")
            return False
    print("Word " + word + " contains all of the yellow letters- returning True!")
    return True


guess = 'arose'
previous_guesses = []

# N for Not In Word
# Y for Yellow (in word somewhere)
# G for Green (in word at this index)

acceptable_states = ['N', 'Y', 'G']

for i in range(1, 7):
    print("Try '" + guess + "'.")
    previous_guesses.append(guess)

    yellow_letters = {}

    for j in range(0, 5):
        tile_state = input("What colour was the '" + guess[j] + "' tile? (N/Y/G)? ").upper()

        if tile_state == 'Y':
            yellow_letters[j] = guess[j]
            guess = guess[0:j] + '*' + guess[j + 1:len(guess)]
        elif tile_state == 'N':
            guess = guess[0:j] + '*' + guess[j+1:len(guess)]
        elif tile_state == 'G':
            guess = guess[0:j] + guess[j] + guess[j + 1:len(guess)]

        print(guess)


    # Now find all the words that fit the criteria:
    # 1. They have not been guessed before ✅
    # 2. They have the green letters in the correct indices ✅
    # 3. They have the yellow letters in them somewhere (but not at the same index as previous guess)
    # And order them by letter frequency
    # Finally set guess to the most likely guess

    possible_words = find_possible_words(guess, yellow_letters)