import numpy as np
from scipy.ndimage.filters import minimum_filter
from scipy.ndimage.measurements import label, labeled_comprehension
from scipy.ndimage.morphology import (
    binary_erosion,
    generate_binary_structure,
)
from matplotlib import pyplot as plt

with open("./input_09.txt", "r") as f:
    data = f.readlines()

data = list(map(lambda string: list(string)[:-1], data))
data = np.array(data, dtype=int)

## Test data
# data = np.array(
#     [
#         [2, 1, 9, 9, 9, 4, 3, 2, 1, 0],
#         [3, 9, 8, 7, 8, 9, 4, 9, 2, 1],
#         [9, 8, 5, 6, 7, 8, 9, 8, 9, 2],
#         [8, 7, 6, 7, 8, 9, 6, 7, 8, 9],
#         [9, 8, 9, 9, 9, 6, 5, 6, 7, 8],
#     ]
# )

# Part 1

## IVAN's detect peaks function
def detect_local_minima(data):
    neighborhood = generate_binary_structure(len(data.shape), 1)
    local_min = minimum_filter(data, footprint=neighborhood) == data
    background = data == 9
    eroded_background = binary_erosion(
        background, structure=neighborhood, border_value=1
    )
    detected_minima = local_min ^ eroded_background
    return np.where(detected_minima), detected_minima


minima_coords, minima = detect_local_minima(data)
risk_levels = data[minima_coords] + 1
print("Sum of risk levels:", risk_levels.sum())


# Part 2
## Image analysis comtinues!

basins = (data != 9).astype(int)

neighborhood = generate_binary_structure(2, 1)
labeled_basins, n_components = label(basins, neighborhood)

sizes = [0] * n_components
for i in range(n_components):
    sizes[i] += (labeled_basins == i).sum()

sizes = sorted(sizes)
print("Product of largest basins:", sizes[-2] * sizes[-3] * sizes[-4])
