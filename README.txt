
ncaa.py:
This program generates results for filling out a 2021 NCAA march madness bracket using the logic that a given team's chance to win is proportional to the ratio of its seed to the seed of the team it's playing.
E.g. If a 2 seed plays a 15 seed, the 2 seed has a 15/17 chance of winning.
If that 2 seed later plays a 1 seed, it has a 1/3 chance of winning.
Matchups between same-seeded teams are a coinflip.
Random numbers are generated using python's random library. Updated for the 2022 tourament.

bracket_analyzer.py:
This is the main program to analyze historical bracket data. It uses the sportsipy api. There should be a few comments to make sense of the code.

graph.py:
I took the output of the analysis and copied it into a few lists in this file. This graphs the data.

sorter.py:
This was just me learning how to sort the data.
