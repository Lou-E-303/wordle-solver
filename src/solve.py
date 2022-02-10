import sys

from utils.find_possible_words import find_possible_words
from utils.suggest_next_guess import suggest_next_guess

guess = "alert"
previous_guesses = []
green_letters = []
yellow_letters = {}
grey_letters = {}
WORD_LENGTH = 5
NUMBER_OF_GUESSES = 6


def take_input():
    print("\nTry '" + guess + "'.")

    user_input = input("\nPlease enter the result you got back from Wordle. \n"
                       "Use G for Green, Y for Yellow and X for Grey. \n"
                       "For example, if you entered 'arose' and the R and S were \n"
                       "yellow and green respectively, you should enter XYXGX. \n"
                       "\nEnter your result now: ").upper()

    return user_input


def validate_input(user_input):
    if len(user_input) != 5:
        print("\nInput invalid! Please enter only five letters. \n")
        return False

    for letter in user_input:
        if letter != "G" and letter != "Y" and letter != "X":
            print("\nInput invalid! Please only enter G for Green, Y for Yellow and X for Grey.")
            return False

    return True


def check_win(result):
    if result == 'GGGGG':
        print("\nCongrats on the win! 🎉")
        sys.exit()


def process_guess_letters(new_guess, result):
    for j in range(WORD_LENGTH):
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


if __name__ == "__main__":
    for i in range(NUMBER_OF_GUESSES):
        previous_guesses.append(guess)

        input_invalid = True

        while input_invalid:
            wordle_result = take_input()
            input_invalid = not validate_input(wordle_result)

        check_win(wordle_result)

        guess = process_guess_letters(guess, wordle_result)

        possible_words = find_possible_words(guess, yellow_letters, grey_letters, green_letters, previous_guesses)

        guess = suggest_next_guess(possible_words)


