from find_possible_words import find_possible_words


guess = 'arose'
previous_guesses = []

# N for Not In Word
# Y for Yellow (in word somewhere)
# G for Green (in word at this index)

acceptable_states = ['GREY', 'YELLOW', 'GREEN']

for i in range(1, 7):
    print("Try '" + guess + "'.")
    previous_guesses.append(guess)

    yellow_letters = {}

    for j in range(0, 5):
        tile_state = input("What colour was the '" + guess[j] + "' tile? (GREY/YELLOW/GREEN)? ").upper()

        if tile_state == 'YELLOW':
            yellow_letters[j] = guess[j]
            guess = guess[0:j] + '*' + guess[j + 1:len(guess)]
        elif tile_state == 'GREY':
            guess = guess[0:j] + '*' + guess[j+1:len(guess)]
        elif tile_state == 'GREEN':
            guess = guess[0:j] + guess[j] + guess[j + 1:len(guess)]

        print(guess)

    possible_words = find_possible_words(guess, yellow_letters, previous_guesses)

    # Now order possible guesses by letter frequency
    # Finally set guess to the most likely guess