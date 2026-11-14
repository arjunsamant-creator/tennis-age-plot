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

(Write your own reflections here.)
