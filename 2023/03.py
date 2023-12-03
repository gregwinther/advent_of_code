import re

## Part I

# test_data = """467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598.."""
# 
# lines = test_data.split("\n")

lines = list(open("./input03.txt"))

N = len(lines[0]) - 1 # Width (x-coords). Remove line change char.
M = len(lines) # Height (y-coords) 

# Create dict[coords]: []
# coords are limited to where not digits or .
# Coordinates of special symbols and part
# numbers associated with them in list.
symbols = dict()
for x in range(N):
    for y in range(M):
        symbol = lines[y][x]
        if lines[y][x] not in "0123456789.":
            symbols[(x, y)] = []

# Run through cols
for i, row in enumerate(lines):
    # find all numbers in col
    for dig in re.finditer(r"\d+", row):
        # Coordinates of number
        search_area = {(x, y) for x in range(dig.start() - 1, dig.end() + 1) for y in [i - 1, i, i + 1]}
        # print(search_area & symbols.keys())
        # Mask search area with allowed areas, i.e. "not_digits"
        # store found number in symbols dict
        for coords in search_area & symbols.keys():
            symbols[coords].append(int(dig.group()))

print("Part numbers sum: ", sum([sum(sym) for sym in symbols.values()]))

## Part II
from math import prod
print(
    "Sum of gear ratios: ",
    sum([prod(sym) for sym in symbols.values() if len(sym) == 2])
)