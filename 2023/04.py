import re

# test_input = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
# Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
# Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
# Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
# Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
# Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
# """
# 
# lines = test_input.split("\n")
# lines = lines[:-1]

with open("./input04.txt") as f:
    lines = f.readlines()

game_points = {}
for i, line in enumerate(lines):
    line = re.sub(r"Card \d+: ", "", line)
    winning_numbers, your_numbers = line.split("|")
    winning_numbers = re.findall(r"\d{1,2}", winning_numbers)
    your_numbers = re.findall(r"\d{1,2}", your_numbers)
    winning_numbers = set(map(int, winning_numbers))
    your_numbers = set(map(int, your_numbers))
    wins = your_numbers & winning_numbers
    n_wins = len(wins)
    if n_wins > 0: 
        game_points[i] = 2**(n_wins - 1)
    else:
        game_points[i] = 0

print("Total points: ", sum(game_points.values()))