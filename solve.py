from utils.find_possible_words import find_possible_words
from utils.suggest_next_guess import suggest_next_guess

guesses = [('arose', 31320), ('irate', 28597), ('steam', 27826)]
previous_guesses = []
yellow_letters = {}
grey_letters = []
green_letters = []

for i in range(1, 7):
    print(guesses)
    guess = guesses[0][0]
    print("Try '" + guess + "', or one of the other top guesses listed above.")

    guess = input("What guess did you choose? ")
    guess = guess.lower()

    previous_guesses.append(guess)

    result = input("\n\nPlease enter the result you got back from Wordle. \n"
                   "Use N for Not In Word, Y for Yellow and G for Green. \n"
                   "For example, if you entered 'arose' and the R and S were \n"
                   "yellow and green respectively, you should enter NYNGN. \n"
                   "\nEnter your result now: ")

    for j in range(0, 5):
        if result[j] == 'Y':
            yellow_letters[j] = guess[j]
            guess = guess[0:j] + '*' + guess[j + 1:len(guess)]
        elif result[j] == 'N':
            if (guess[j] not in yellow_letters.values()) and (guess[j] not in green_letters):
                grey_letters.append(guess[j])
            guess = guess[0:j] + '*' + guess[j+1:len(guess)]
        elif result[j] == 'G':
            green_letters.append(guess[j])
            guess = guess[0:j] + guess[j] + guess[j + 1:len(guess)]

    print(guess)

    possible_words = find_possible_words(guess, yellow_letters, grey_letters, previous_guesses)

    guesses = suggest_next_guess(possible_words)