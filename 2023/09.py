import numpy as np

test_input = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45
"""

puzzle_input = test_input.strip()

with open("./input09.txt") as f:
    puzzle_input = f.read().strip()

lines = []
for line in puzzle_input.split("\n"):
    numbers = [int(number) for number in line.split()]
    lines.append(numbers)

extr_numbers = []
extr_numbers2 = []
for line in lines:
    pyramid = [] 
    steps = line.copy()
    while np.any(steps):
        pyramid.append(steps)
        steps = list(np.diff(steps))

    extr_number = 0
    extr_number2 = 0
    for layer in pyramid[::-1]:
        extr_number += layer[-1]
        extr_number2 = layer[0] - extr_number2 

    extr_numbers.append(extr_number)
    extr_numbers2.append(extr_number2)

print("Sum of extrapolated values (part one): ", sum(extr_numbers)) 
print("Sum of extrapolated values (part two): ", sum(extr_numbers2))
