Wordle Solver v0.1
=============

# Intro:

A program which tries to solve [Wordle](https://www.powerlanguage.co.uk/wordle/) puzzles as efficiently as possible. Perfection would be nice but really I'd just like this thing to be able to solve it better than me.

In `scripts/` you will find a few short scripts I used to organise the data, work out which word our solver should begin with and so on.

Dictionary text file found [here](https://raw.githubusercontent.com/powerlanguage/word-lists/master/word-list-raw.txt) with thanks to Wordle creator [Josh Wardle](https://github.com/powerlanguage).

# Run:

Run `python3 solve.py`.

This will provide you with a reasonable (near-optimal, I think) first guess and then ask you to input the colours of the tiles once your guess has been made. It will then provide its best guess at the word based upon letter frequencies of five-letter words in English using the information it has from your previous guesses.

# Changelog

- **Jan 4th:** v0.1 up and running!

# License:

Do what you want with it.




