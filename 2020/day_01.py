import numpy as np

with open("./input.txt") as f:
    lines = f.readlines()

lines = list(map(lambda line: int(line.rstrip("\n")), lines))

n = len(lines)

all_sums = np.zeros((n, n))

for i in range(n):
    for j in range(i + 1, n):
        all_sums[i, j] = lines[i] + lines[j]
        if int(lines[i] + lines[j]) == 2020:
            answer = lines[i] * lines[j]
    # break


# print(all_sums)
diff_array = np.abs(all_sums - 2020)
idx = np.unravel_index(np.argmin(diff_array, axis=None), diff_array.shape)
print(idx)
print(all_sums[idx])
print(f"The answer is {answer}")

