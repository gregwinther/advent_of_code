import numpy as np 

# positions = np.array([16,1,2,0,4,2,7,1,2,14], dtype=int)
positions = np.loadtxt("./input_07.txt", dtype=int, delimiter=",")
cost = np.abs(positions - np.median(positions)).sum()
print(f"Part 1 sol'n: {int(cost):15}")

# Part 2: Fuel cost increase. First step cost 1, second cost 2 etc
## Create matrix crab vs distance to every other?
## A factorial, but with addition is the binomial coefficient
## n(n + 1) / 2

n = len(positions)
m = positions.max() + 1
possible_positions = np.arange(m)
distances = np.zeros((n, m))
for i in range(n):
    distances[i, :] = np.abs(positions[i] - possible_positions)

# Scale distances properly
distances = distances * (distances + 1) / 2

costs = distances.sum(axis=0)
print(f"Part 2 sol'n: {int(costs.min()):15}")
