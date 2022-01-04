Wordle Solver v0.1
=============

# Intro:

A program which tries to solve [Wordle](https://www.powerlanguage.co.uk/wordle/) puzzles as efficiently as possible. Perfection would be nice but really I'd just like this thing to be able to solve it better than me.

In `scripts/` you will find a few short scripts I used to organise the data, work out which word our solver should begin with and so on.

Dictionary text file found [here](https://raw.githubusercontent.com/powerlanguage/word-lists/master/word-list-raw.txt) with thanks to Wordle creator [Josh Wardle](https://github.com/powerlanguage).

# Setup:

***There's no need to generate the data as I've done it for you***, but if you want to delete all the resources (except word_list.txt) and see for yourself how it works:

Run `python3 scripts/generate_five_letter_words.py` in your terminal.

Do this twice - once as normal and once without the newline `+"/n"` here: `five_letter_words.write(word+"\n")`(and with a new filename).

This will give you the five letter words in both formats needed for the scripts to work (I'm lazy sorry)

And that should be it, you're good to go!

# Run:

Run `python3 solve.py`.

This will provide you with a reasonable (near-optimal, I think) first guess and then ask you to input the colours of the tiles once your guess has been made. It will then provide its best guess at the word based upon letter frequencies of five-letter words in English using the information it has from your previous guesses.

# Changelog

- **Jan 4th:** v0.1 up and running!

# License:

Do what you want with it.




