import sys
import random

from utils.find_possible_words import find_possible_words
from utils.suggest_next_guess import suggest_next_guess

guess = "alert"
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
    print("\nTry '" + guess + "'.")

    previous_guesses.append(guess)

    result = input("\nPlease enter the result you got back from Wordle. \n"
                   "Use G for Green, Y for Yellow and X for Grey. \n"
                   "For example, if you entered 'arose' and the R and S were \n"
                   "yellow and green respectively, you should enter XYXGX. \n"
                   "\nEnter your result now: ").upper()

    if result == 'GGGGG':
        print("\nCongrats on the win! 🎉")

        if random.random() < 0.8:
            print("\nActually, you did nothing of value except to input my answers.")
            print("You are only slightly more worthy of praise than a mindless chimp.")

        sys.exit()

    guess = process_guess_letters(guess)

    possible_words = find_possible_words(guess, yellow_letters, grey_letters, green_letters, previous_guesses)

    guess = suggest_next_guess(possible_words)
