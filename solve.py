from scripts.load_words import load_words

guess = 'arose'
previous_guesses = []

for i in range(1, 7):
    print("Try '" + guess + "'.")
    previous_guesses.append(guess)

    acceptable_states = ['A', 'N', 'Y', 'G']

    # A for Available
    # N for Not In Word
    # Y for Yellow (in word somewhere)
    # G for Green (in word at this index)

    result = {
        0: "A",
        1: "A",
        2: "A",
        3: "A",
        4: "A"
    }

    for j in range(0, 5):
        tile_state = input("What colour was the '" + guess[j] + "' tile? (N/Y/G)? ")

        if tile_state in acceptable_states:
            result[j] = tile_state
        else:
            print("Some error message or other and retry - TODO")

    # Now find all the words that fit the criteria:
    # 1. They have not been guessed before ✅
    # 2. They have the green letters in the correct indices
    # 3. They have the yellow letters in them somewhere
    # And order them by letter frequency
    # Finally set guess to the most likely guess

#     possible_words = find_possible_words(result)
#
#
# def find_possible_words(result):
#     five_letter_words = load_words('../resources/five_letter_words.txt')
#     for word in five_letter_words:
#         if word in previous_guesses:
#             five_letter_words.remove(word)
#
