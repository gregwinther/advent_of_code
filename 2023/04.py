import re

test_input = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
"""

lines = test_input.split("\n")
lines = lines[:-1]

# with open("./input04.txt") as f:
#     lines = f.readlines()

## Part One

game_points = {}
matching_numbers = {}
for i, line in enumerate(lines):
    line_ = re.sub(r"Card[ ]{1,3}\d+: ", "", line)
    winning_numbers, your_numbers = line_.split("|")
    winning_numbers = re.findall(r"\d{1,2}", winning_numbers)
    your_numbers = re.findall(r"\d{1,2}", your_numbers)
    your_numbers = set(map(int, your_numbers))
    winning_numbers = set(map(int, winning_numbers))
    matches = your_numbers & winning_numbers
    n_matches = len(matches)
    if n_matches > 0: 
        points = 2**(n_matches - 1)
    else:
        points = 0

    matching_numbers[i] = n_matches
    game_points[i] = points

print("Total points: ", sum(game_points.values()))

## Part Two

# Some sort of recursion??

def find_additional_cards(index, n_cards, index_limit=208):
    additional_cards = dict.fromkeys(matching_numbers, 0)
    if index + n_cards > index_limit:
        n_cards = index - index_limit
    for i in range(index + 1, index + n_cards + 1):
        additional_cards[i] += 1
    return additional_cards

N = len(matching_numbers)

# find the sinks!
sinks = set([i for i in matching_numbers if matching_numbers[i] == 0])

add_matching_numbers = dict.fromkeys(matching_numbers.keys())
for i, n_matches in matching_numbers.items():
    all_additional_cards = [] 
    add_cards = find_additional_cards(i, n_matches, N)
    new_relevant_cards = {i: n for i, n in add_cards.items() if i not in sinks and n > 0}