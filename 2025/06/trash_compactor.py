import numpy as np

# file_path = "./test_input.txt"
file_path = "./input.txt"

def part_one():
    with open(file_path, "r") as file:
        lines = file.readlines()

    operations = lines.pop(-1)
    operations = operations.rstrip().split(" ")
    operations = [op.strip() for op in operations if op in ["*", "+"]]

    lines = [line.rstrip().split(" ") for line in lines]
    numbers = []
    for line in lines:
        number_line = []
        for obs in line:
            if len(obs) == 0:
                continue
            else:
                number_line.append(int(obs))
        numbers.append(number_line)
    numbers = np.array(numbers)

    answers = []
    for i, operation in enumerate(operations):
        if operation == "*":
            answer = np.prod(numbers[:, i])
        elif operation == "+":
            answer = np.sum(numbers[:, i])
        answers.append(answer)

    print("Grandt total :", sum(answers))

def part_two():
    with open(file_path, "r") as file:
        lines = file.readlines()

    # The problem should be read right to left, one _column_ at a time
    # First split every character into its own list element
    lines = [list(line.rstrip("\n")) for line in lines]
    problem_array = np.array(lines)

    # For last row, get the operations only
    operations = problem_array[-1, :]
    operations = [op for op in operations if op in ["*", "+"]]
    problem_array = problem_array[:-1, :]

    # Start from the rightmost column and move left
    # For each column, combine elements into a number
    # If there are only spaces in a column,
    # it means that we have reach the end of the collection of numbers

    numbers = []
    numbers_subset = []

    for col_idx in range(problem_array.shape[1]-1, -1, -1):
        column = problem_array[:, col_idx]
        # Combine column elements into numbers
        if all(char == " " for char in column):
            numbers.append(numbers_subset)
            numbers_subset = []
            continue
        number = int("".join(column))
        numbers_subset.append(number)
    numbers.append(numbers_subset)

    # Apply operations to sub-lists
    answers = []
    for i, operation in enumerate(operations[::-1]):
        if operation == "*":
            result = np.prod(numbers[i])
        elif operation == "+":
            result = np.sum(numbers[i])
        answers.append(result)

    print("Grand total (part two):", sum(answers))

part_one()
part_two()