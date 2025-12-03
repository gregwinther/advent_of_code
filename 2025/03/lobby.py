import numpy as np

# file_path = "./test_input.txt"
file_path = "./input.txt"

with open(file_path, "r") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]

max_joltages = []

for line in lines:
    # print(line)
    n = len(line)
    pruned_line = line[:-1]
    last_int = int(line[-1])
    line_array = np.array([int(ch) for ch in line])
    pruned_line_array = np.array([int(ch) for ch in pruned_line])
    max_pos_1 = pruned_line_array.argmax()
    max_1 = line[max_pos_1]
    if max_pos_1 + 1 == n - 1:
        max_2 = line[-1] 
    else:
        max_2 = line_array[max_pos_1 + 1:].max()

    max_joltages.append(int(max_1 + str(max_2))) 

print("Joltages:", max_joltages)
print("Sum:", sum(max_joltages))
