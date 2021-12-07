import numpy as np 

# Test case
positions = np.array([16,1,2,0,4,2,7,1,2,14], dtype=int)

cost = np.abs(positions - np.median(positions)).sum()
print(cost)