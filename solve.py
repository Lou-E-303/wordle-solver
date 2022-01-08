from utils.find_possible_words import find_possible_words
from utils.suggest_next_guess import suggest_next_guess

possible_guesses = [('alert', 4559), ('later', 4559), ('arose', 4534), ('irate', 4511), ('aisle', 4271), ('ratio', 4032)]
previous_guesses = []
yellow_letters = {}
grey_letters = []
green_letters = []


def process_guess_letters(guess):
    for j in range(0, 5):
        if result[j] == 'Y':
            yellow_letters[j] = guess[j]
            guess = guess[0:j] + '*' + guess[j + 1:len(guess)]
        elif result[j] == 'X':
            if (guess[j] not in yellow_letters.values()) and (guess[j] not in green_letters):
                grey_letters.append(guess[j])
            guess = guess[0:j] + '*' + guess[j + 1:len(guess)]
        elif result[j] == 'G':
            green_letters.append(guess[j])
    return guess


for i in range(1, 7):
    for guess in reversed(possible_guesses):
        print(guess)

    guess = possible_guesses[0][0]
    print("\nTry '" + guess + "', or one of the other top guesses listed above.")

    guess = input("\nWhat guess did you choose? ").lower()

    previous_guesses.append(guess)

    result = input("\nPlease enter the result you got back from Wordle. \n"
                   "Use G for Green, Y for Yellow and X for Grey. \n"
                   "For example, if you entered 'arose' and the R and S were \n"
                   "yellow and green respectively, you should enter XYXGX. \n"
                   "\nEnter your result now: ").upper()

    guess = process_guess_letters(guess)

    print(guess)

    possible_words = find_possible_words(guess, yellow_letters, grey_letters, previous_guesses)

    possible_guesses = suggest_next_guess(possible_words)
