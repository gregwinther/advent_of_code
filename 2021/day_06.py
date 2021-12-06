import numpy as np

# Lanternfish. Part 1

with open("./input_06.txt", "r") as f:
    state = f.readlines()[0]
    state = np.array(state.split(","), dtype=int)


# Test state
# state = np.array([3,4,3,1,2])
cycles = 80

for i in range(cycles):
    state -= 1
    new_fish = np.array((state < 0).sum() * [8])
    end_cycle_ind = np.where(state < 0)
    state[end_cycle_ind] += 7
    state = np.append(state, new_fish)
    print(f"{i+1:2}: {len(state):30} lanternfish")
