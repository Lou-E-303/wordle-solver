import sys
from utils.find_possible_words import find_possible_words
from utils.suggest_next_guess import suggest_next_guess

possible_guesses = [('alert', 6), ('raise', 5), ('later', 4), ('arose', 3), ('irate', 2), ('aisle', 1), ('ratio', 0)]
previous_guesses = []
yellow_letters = {}
grey_letters = {}
green_letters = []


def process_guess_letters(new_guess):
    for j in range(0, 5):
        if result[j] == 'Y':
            yellow_letters[j] = new_guess[j]
            new_guess = new_guess[0:j] + '*' + new_guess[j + 1:len(new_guess)]
        elif result[j] == 'X':
            if j in grey_letters:
                grey_letters[j].append(new_guess[j])
            else:
                grey_letters[j] = [new_guess[j]]
            new_guess = new_guess[0:j] + '*' + new_guess[j + 1:len(new_guess)]
        elif result[j] == 'G':
            green_letters.append(new_guess[j])
    return new_guess


for i in range(1, 7):
    for guess in reversed(possible_guesses):
        print(guess)

    if len(possible_guesses) > 0:
        guess = possible_guesses[0][0]

    print("\nTry '" + guess + "', or one of the other top guesses listed above.")

    guess = input("\nWhat guess did you choose? ").lower()

    previous_guesses.append(guess)

    result = input("\nPlease enter the result you got back from Wordle. \n"
                   "Use G for Green, Y for Yellow and X for Grey. \n"
                   "For example, if you entered 'arose' and the R and S were \n"
                   "yellow and green respectively, you should enter XYXGX. \n"
                   "\nEnter your result now: ").upper()

    if result == 'GGGGG':
        print("\nCongrats on the win! 🎉 \n")
        sys.exit()

    guess = process_guess_letters(guess)

    print(guess)

    possible_words = find_possible_words(guess, yellow_letters, grey_letters, green_letters, previous_guesses)

    possible_guesses = suggest_next_guess(possible_words)
