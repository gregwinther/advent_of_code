import numpy as np

def find_joltage(line, num_digits):
    selected = []
    left = 0 # Start. Can only pick after the one just picked

    # Scan the rest with "safety buffer".
    for right in range(len(line) - num_digits + 1, len(line) + 1):
        # Get slice from left to safety buffer
        current_window = line[left:right]
        # Find highest value
        best_digit = max(current_window)
        # Find pos of that digit relative to current pos
        distance_to_digit = line[left:].index(best_digit)
        # Advance left pointer
        left += distance_to_digit + 1
        # Append best digit to selected
        selected.append(line[left - 1])

    return int("".join(selected))

# file_path = "./test_input.txt"
file_path = "./input.txt"

joltage_sum = 0
with open(file_path, "r") as f:
    for line in f:
        # print(line.rstrip())
        joltage = find_joltage(line.rstrip(), 12)
        # print("Joltage:", joltage)
        joltage_sum += joltage
print("Sum:", joltage_sum)
