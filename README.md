# Letter Combinations Generator

This project implements a solution to generate all possible letter combinations
for a given digit string (2–9), based on a phone keypad mapping.

## Problem

Input: a string of digits (2–9)  
Output: all possible letter combinations

Example:
```
Input: "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
```
## Solution

The solution uses **backtracking** to generate all combinations.

- Each digit maps to multiple letters
- We recursively build combinations
- When a combination is complete, it is added to the result

## Structure
```
src/letter_combinations/solution.py
tests/test_solution.py
main.py
```
## Setup

### Windows
```
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```
### Linux/Mac
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```
## Run
```
python main.py 23
```
## Tests
```
pytest
```
## Notes
- Handles empty input by returning an empty list.
- Output is generated in a deterministic order based on the backtracking traversal.
- The solution assumes valid input according to the assignment constraints.
