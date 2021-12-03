import numpy as np 

data = np.loadtxt("./input_03.txt", dtype=str)
data = np.array(list(map(list, data)), dtype=int)

gamma_rate = np.round(data.sum(axis=0) / data.shape[0]).astype(int)
epsilon_rate = np.logical_not(gamma_rate).astype(int)

gamma_rate = int("".join(list(gamma_rate.astype(str))), 2)
epsilon_rate = int("".join(list(epsilon_rate.astype(str))), 2)

print(f"Answer: {gamma_rate * epsilon_rate}")