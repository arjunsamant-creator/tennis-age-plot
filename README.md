# tennis-age-plot

Python package that downloads a tennis player's career matches from
tennisabstract.com and plots player age vs. age difference with opponents.

## Install

pip install git+https://github.com/arjunsamant-creator/tennis-age-plot.git

## Usage

from tennisage import get_player_matches, plot_age_gap

serena = get_player_matches("serena williams")
plot_age_gap(serena)

rafa = get_player_matches("Rafael Nadal")
plot_age_gap(rafa)

get_player_matches("GastonSanchez")  # raises a clear error

## Reflections

The biggest lesson was how much structure matters. Splitting the work into small private functions (build the URL, download, pull out the match rows, calculate ages) made each piece easy to test and kept every function under 20 lines. The data was messier than the assignment's sample files suggested. Women's files give the opponent's birth date while men's files give an age, and Nadal's file actually mixes both, so the code has to decide row by row instead of player by player. My first regex for pulling the match list out of the JavaScript only worked on the sample data, because the real file has line breaks before the closing bracket. I only caught that by testing against the real file, which taught me not to trust sample data alone. I also learned that a player's own birth date is not in the career file at all. It lives in a second file, so the package downloads two files per player. The tests use small pasted samples so they never touch the live website, which keeps them fast and reliable. Committing one small step at a time made it easy to see what changed and to fix mistakes without breaking everything else.
