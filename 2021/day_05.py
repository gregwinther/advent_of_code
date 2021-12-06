import numpy as np
from matplotlib import pyplot as plt

# Part 1
with open("./input_05.txt", "r") as f:
    data = f.readlines()

data = list(
    map(
        lambda string: list(
            map(int, string.replace(" -> ", ",").split(","))
        ),
        data,
    )
)
data = np.array(data)
grid = np.zeros([data.max()] * 2)

for coords in data:
    x1, y1, x2, y2 = coords

    # Only vertical
    if x1 == x2:
        if y1 < y2:
            grid[x1, y1 : y2 + 1] += 1
        elif y1 > y2:
            grid[x1, y2 : y1 + 1] += 1
        else:
            grid[x1, y1] += 1
        continue

    # Only horizontal
    if y1 == y2:
        if x1 < x2:
            grid[x1 : x2 + 1, y1] += 1
        elif x1 > x2:
            grid[x2 : x1 + 1, y1] += 1
        continue

    # Diagonals (Part 2)
    if x1 < x2 and y1 < y2:
        grid[np.arange(x1, x2 + 1), np.arange(y1, y2 + 1)] += 1
    elif x1 < x2 and y1 > y2:
        grid[np.arange(x1, x2 + 1), np.arange(y1, y2 - 1, -1)] += 1
    elif x1 > x2 and y1 < y2:
        grid[np.arange(x1, x2 - 1, -1), np.arange(y1, y2 + 1)] += 1
    elif x1 > x2 and y1 > y2:
        grid[np.arange(x1, x2 - 1, -1), np.arange(y1, y2 - 1, -1)] += 1

plt.imshow(grid)
plt.show()

intersections = (grid > 1).sum()
print("No. of intersections:", intersections)
