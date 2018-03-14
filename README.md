# BI Contest 2018

## Description

Some of the algorithms that I most enjoyed to produce as solutions to problems in Bioinformatics Contest 2018.

## realMaxATP.py

Provided a **txt** file containing a list of glucose and oxygen integer prices (per mol), along with a limit budget (in same currency), it uses a heuristic algorithm to approximate the glucose and oxygen mol quantities that maximize ATP payoff (via fermentation and/or aerobic respiration) while still fitting the budget given. Returns the maximum resulting ATP amount (mols).

call: `python3 realGOBalance.py <input.txt>`

**Example input:**

	2 4 10
	7 5 23

Meaning...

Scenario | Glucose Price | Oxygen Price | Budget
-------- | ------------- | ------------ | ------
A | 2 | 4 | 10
B | 7 | 5 | 23

## intMaxATP.py

Same as realGOBalance, but solves the problem when it is only possible to buy integer amounts of glucose and oxygen mols, hence returning a maximum resulting ATP integer amount.

call: `python3 intGOBalance.py <input.txt>`

## longestTandem.py

Given a **fasta** file containing one or more DNA/RNA/AA sequences, it finds the longest tandem repeat in each sequence and returns its start position (0-based), the length of its first section and the length of the second one (e.g. `243 45 45`). The user can also provide a floating point threshold (from 0.0 up to 1.0) to represent the maximum difference (measured via Levenshtein Distance) tolerated between sections of a repeat. If the threshold provided is positive, the algorithm will be tolerant to some differences caused by insertions, deletions or substitutions; if it is 0, only identical sections in tandem will be considered tandem repeats. In case no threshold is provided, it defaults to 0.1 (max. 10% difference).

call: `python3 longestTandem.py <sequences.fasta> <max-difference-threshold(0.0-1.0)>`