def load_words():
    with open('words_alpha.txt') as word_file:
        valid_words = set(word_file.read().split())

    return valid_words


english_words = load_words()
five_letter_words = open("five_letter_words.txt", "w+")

for word in english_words:
    if len(word) == 5:
        print("Wrote word: " + word)
        five_letter_words.write(word+"\n")

five_letter_words.close()
