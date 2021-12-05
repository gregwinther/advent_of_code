import numpy as np

# Part 1

with open("./input_04.txt") as f:
    lines = [s for s in f if not len(s) <= 1]

numbers = list(map(int, lines[0].split(",")))
lines = lines[1:]
n_lines = len(lines)
blocksize = 5
boards = [
    np.loadtxt(lines[i : i + blocksize], dtype=int)
    for i in range(0, n_lines, blocksize)
]
boards = np.array(boards)
marked = np.zeros_like(boards)

winner = ""
for i, number in enumerate(numbers):
    marked += (boards == number).astype(int)
    colsum = marked.sum(axis=1)
    rowsum = marked.sum(axis=2)
    # Check columns
    col_coords = np.where(colsum==5)
    if len(col_coords[0]) > 0: 
        winner=col_coords[0][0]
        break
    # Check rows 
    row_coords = np.where(rowsum==5)
    if len(row_coords[0]) > 0: 
        winner=row_coords[0][0]
        break

## Compute score
winner_marked_inverse = np.logical_not(marked[winner]).astype(int)
winning_board = boards[winner]
score = numbers[i] * np.tensordot(winning_board, winner_marked_inverse)
print(f"Score: {score}")