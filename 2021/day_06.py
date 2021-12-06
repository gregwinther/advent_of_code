import numpy as np
from collections import Counter

# Lanternfish. Part 1

# Test state
# state = np.array([3,4,3,1,2])
cycles = 256

def stupid_way(state, cycles):
    for i in range(cycles):
        state -= 1
        new_fish = np.array((state < 0).sum() * [8])
        end_cycle_ind = np.where(state < 0)
        state[end_cycle_ind] += 7
        state = np.append(state, new_fish)
        print(f"{i+1:2}: {len(state):30} lanternfish")

# There's a smarter way. Part 2.
def hopefully_smarter_way(state, cycles):
    c = Counter(state)
    state = [0] * 9 
    for i in range(9):
        state[i] = c[i]

    new_fish = 0
    for i in range(cycles):
        new_fish = state[0]
        for j in range(1, 9):
            state[j - 1] = state[j]
        state[6] += new_fish 
        state[-1] = new_fish
    
        print(f"{i+2:3}: {sum(state):30}") 

if __name__ == "__main__":
    with open("./input_06.txt", "r") as f:
        state = f.readlines()[0]
        state = np.array(state.split(","), dtype=int)

    # stupid_way(state, 80)
    hopefully_smarter_way(state, 256)