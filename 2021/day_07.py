import numpy as np 

# positions = np.array([16,1,2,0,4,2,7,1,2,14], dtype=int)
positions = np.loadtxt("./input_07.txt", dtype=int, delimiter=",")
cost = np.abs(positions - np.median(positions)).sum()
print(f"Part 1 sol'n: {cost}")