import numpy as np

# file_path = "./test_input.txt"
file_path = "./input.txt"

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