Wordle Solver v0.1
=============

# Intro:

A program which tries to solve [Wordle](https://www.powerlanguage.co.uk/wordle/) puzzles efficiently.

# Run:

Run `python3 solve.py`.

This will provide you with a reasonable first guess<sup>1</sup> and then ask you to input the colours of the tiles once your guess has been made. It will then provide its best guess at the word based upon letter frequencies of five-letter words in English using the information it has from your previous guesses.

<sup>1</sup> This solver is stubborn - it won't use any word as a guess which is not a valid answer. Technically, there are [<u>better</u>](https://matt-rickard.com/wordle-whats-the-best-starting-word/) first [<u>guesses</u>](https://www.theringer.com/2022/1/7/22870249/what-to-do-when-playing-the-word-game-wordle-isnt-enough-solve-it).
# Changelog

- **Jan 4th:** v0.1 up and running!
- **Jan 5th:** Added better input method
- **Jan 8th:** Added official Wordle dictionary
- **Jan 16th:** Fixed major bug where grey letters weren't being discounted properly
- **Feb 10th:** Fixed similar bug as above, v1.0 now up and running! 🥳

[Trello Board.](https://trello.com/b/6UknNHIy/wordle-solver)

# License:

Do what you want with it.




