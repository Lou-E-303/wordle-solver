guess = 'arose'

for i in range(1, 6):
    print("Try '" + guess + "'.")

    acceptable_states = ['A', 'N', 'Y', 'G']

    # A for Available
    # N for Not In Word
    # Y for Yellow (in word somewhere)
    # G for Green (in word at this index)

    result = {
        guess[0]: "A",
        guess[1]: "A",
        guess[2]: "A",
        guess[3]: "A",
        guess[4]: "A"
    }

    for j in range(0, 5):
        tile_state = input("What colour was the '" + guess[j] + "' tile? (N/Y/G)? ")

        if tile_state in acceptable_states:
            result[guess[j]] = tile_state
        else:
            print("Some error message or other and retry - TODO")

        # Now find all the words that fit the criteria:
        # 1. They have the yellow letters in them somewhere
        # 2. They have the green letters in the correct indices
        # 3. They have not been guessed before
        # And order them by letter frequency
        # Finally set guess to the most likely guess
