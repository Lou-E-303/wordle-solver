def load_all_words(filename):
    with open(filename) as word_file:
        valid_words = set(word_file.read().split())

    return valid_words
