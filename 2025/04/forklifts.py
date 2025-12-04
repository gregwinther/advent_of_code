import numpy as np

# input_path = "./test_input.txt"
input_path = "./input.txt"

with open(input_path, "r") as file:
    lines = file.readlines()
    lines = [list(line.strip()) for line in lines]
    paper_map = np.array(lines)

m, n = paper_map.shape

# Check N, NE, E, SE, S, SW, W, NW for "@" and count steps to "."

def check_direction(start_i, start_j, delta_i, delta_j):
    i, j = start_i + delta_i, start_j + delta_j
    if (i < 0 or i >= m or j < 0 or j >= n):
        return 0
    elif paper_map[i, j] == ".":
        return 0
    elif paper_map[i, j] == "@":
        return 1

# print(paper_map)

good_positions = []

for i in range(m):
    for j in range(n):
        if paper_map[i, j] == ".":
            continue
        # Check each direction. Check how far I can move (not outside map)
        # If there are fewer than four "@" in all directions combined, save pos (good_positions)
        total_at_count = 0
        directions = [(-1, 0), (-1, 1), (0, 1), (1, 1),
                        (1, 0), (1, -1), (0, -1), (-1, -1)]
        for delta_i, delta_j in directions:
            total_at_count += check_direction(i, j, delta_i, delta_j)
        if total_at_count < 4:
            good_positions.append((i, j))

# print("Good Positions:", good_positions)
# # Change map drawing
# for i, j in good_positions:
#     paper_map[i, j] = "X"  # Mark good positions on the map
# print(paper_map)
print("Rolls accesible:", len(good_positions))