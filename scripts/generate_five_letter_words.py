import string

from utils.load_all_words import load_all_words


def word_contains_no_punctuation(word):
    punctuation = string.punctuation
    for i in range(0, len(punctuation)):
        if punctuation[i] in word:
            return False
    return True


english_words = load_all_words('../resources/word_list.txt')
five_letter_words = open("../resources/five_letter_words.txt", "w+")

for word in english_words:
    if len(word) == 5 and word_contains_no_punctuation(word):
        five_letter_words.write(word + "\n")

five_letter_words.close()
