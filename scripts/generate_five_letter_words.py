from load_words import load_words

english_words = load_words('../resources/word_list.txt')
five_letter_words = open("../resources/five_letter_words.txt", "w+")

for word in english_words:
    if len(word) == 5:
        five_letter_words.write(word+"\n")

five_letter_words.close()
