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

winner = 0
for i, number in enumerate(numbers):
    marked += (boards == number).astype(int)
    colsum = marked.sum(axis=1)
    rowsum = marked.sum(axis=2)
    # Check columns
    col_coords = np.where(colsum==5)
    if len(col_coords[0]) > 0: 
        winner = col_coords[0][0]
        break
    # Check rows 
    row_coords = np.where(rowsum==5)
    if len(row_coords[0]) > 0: 
        winner = row_coords[0][0]
        break

## Compute score
winner_marked_inverse = np.logical_not(marked[winner]).astype(int)
winning_board = boards[winner]
score = numbers[i] * np.tensordot(winning_board, winner_marked_inverse)
print(f"Score of first winning board: {score}")

# Part 2: Find last board to win
## Reset marked, create arrays for winning boards.
marked = np.zeros_like(boards)
n_boards = boards.shape[0]

winner = -1
for i, number in enumerate(numbers):
    if n_boards < 1:
        break 
    marked += (boards == number).astype(int)
    colsum = marked.sum(axis=1)
    col_coords = np.where(colsum==5)[0]
    rowsum = marked.sum(axis=2)
    row_coords = np.where(rowsum==5)[0]
    while len(col_coords) > 0 or len(row_coords) > 0:
        if len(col_coords) > 0: 
            # Trick: start with last. Index problem
            winner = col_coords[0] 

        elif len(row_coords) > 0: 
            winner = row_coords[0]

        # Update boards
        if winner >= 0:
            last_winning_board = boards[winner]
            boards = boards[np.arange(n_boards)!=winner]
            last_winning_marked = marked[winner]
            marked = marked[np.arange(n_boards)!=winner]
            n_boards -= 1
            winner = -1

        colsum = marked.sum(axis=1)
        col_coords = np.where(colsum==5)[0]
        rowsum = marked.sum(axis=2)
        row_coords = np.where(rowsum==5)[0]

print()
print("Last winning board:")
print(last_winning_board)
print("Marked cells")
print(last_winning_marked)
print(f"Last number called: {numbers[i-1]}")
winner_marked_inverse = np.logical_not(last_winning_marked).astype(int)
score = numbers[i-1] * np.tensordot(last_winning_board, winner_marked_inverse)
print(f"Score of last winning board: {score}")

