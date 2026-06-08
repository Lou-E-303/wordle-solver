Wordle Solver v2.0
=============

# About

A program which tries to solve [Wordle](https://www.powerlanguage.co.uk/wordle/) puzzles efficiently.

<i>Note: Since the New York Times seems to be making changes to the Wordle dictionary, I probably won't be maintaining this any further, so it may not always work in future.</i>

Some Wordle alternatives which still use the old dictionary (at time of writing 07/03/22):

- [Hello Wordl](https://hellowordl.net/)
- [Werdle](https://demoman.net/etcetera/werdle/)

# Changelog

TODO:

- Benchmark v1.0 and v2.0 against each other, and against a random guesser, to see if V2 is even an improvement over V1.
- Look at the distribution of letter frequencies in each letter position, not just overall
## Version 2

- Applies a penalty for suggested guesses with duplicate letters, which is higher the more duplicate letters there are. This penalty diminishes as the rounds go on.
- Added 'eaves' to the dictionary.
- Handle failures gracefully, and provide a message to the user if no valid guesses are found.
- Output applied score for each word per round.

# Run

Run `python3 src/main.py`.

This will provide you with a reasonable first guess<sup>1</sup> and then ask you to input the colours of the tiles once your guess has been made. It will then provide its best guess at the word based upon letter frequencies of possible answers using the information it has from your previous guesses.

<sup>1</sup> This solver is stubborn - it won't use any word as a guess which is not a valid answer. Technically, there are [<u>better</u>](https://matt-rickard.com/wordle-whats-the-best-starting-word/) [<u>first</u>](https://www.youtube.com/watch?v=v68zYyaEmEA) [<u>guesses</u>](https://www.theringer.com/2022/1/7/22870249/what-to-do-when-playing-the-word-game-wordle-isnt-enough-solve-it).

# Be aware

- I have found at least one example in which the answer is not in the list of valid answers found in this dictionary

# License

Do what you want with it.




