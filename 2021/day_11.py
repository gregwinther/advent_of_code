import numpy as np
from scipy.signal import convolve2d

# Part 1

test_data = np.array(
    [
        [5, 4, 8, 3, 1, 4, 3, 2, 2, 3],
        [2, 7, 4, 5, 8, 5, 4, 7, 1, 1],
        [5, 2, 6, 4, 5, 5, 6, 1, 7, 3],
        [6, 1, 4, 1, 3, 3, 6, 1, 4, 6],
        [6, 3, 5, 7, 3, 8, 5, 4, 7, 8],
        [4, 1, 6, 7, 5, 2, 4, 6, 4, 5],
        [2, 1, 7, 6, 8, 4, 1, 7, 2, 1],
        [6, 8, 8, 2, 8, 8, 1, 1, 3, 4],
        [4, 8, 4, 6, 8, 4, 8, 5, 5, 4],
        [5, 2, 8, 3, 7, 5, 1, 5, 2, 6],
    ]
)

data = test_data

n = 100
flash_count = []
for i in range(n):
    mask = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
    flashed = np.zeros(data.shape, dtype="bool")
    data += 1
    while np.any(flashing := data > 9):
        flashed |= flashing
        data += convolve2d(flashing, mask, mode="same")
        data[flashed] = 0
    flash_count.append(flashed.sum())

print(f"Number of flashed octopi over {n} cycles; {sum(flash_count)}")