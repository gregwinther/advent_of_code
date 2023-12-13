import numpy as np

# test_data = """.....
# .S-7.
# .|.|.
# .L-J.
# .....
# """
# lines = test_data.strip().split("\n")

with open("./input10.txt") as f:
    lines = f.readlines()

data = np.array([[char for char in line.strip()] for line in lines])
data = np.pad(data, 1, constant_values=".")

starting_point = np.argwhere(data == "S")[0]

# Index: (row, col)
pipe_map = {
    "|" : [(-1, 0), ( 1, 0)],
    "-" : [( 0,-1), ( 0, 1)],
    "L" : [(-1, 0), ( 0, 1)],
    "J" : [( 0,-1), (-1, 0)],
    "7" : [( 0,-1), ( 1, 0)],
    "F" : [( 0, 1), ( 1, 0)],
    "." : [], # Will skip in search
    "S" : []
}

# Check directions
def find_valid_directions(
        point, 
        deltas=np.array([(1, 0), (0, 1), (-1, 0), (0,-1)])
    ):
    valid_directions = []
    for delta in deltas:
        possible_matches = pipe_map[data[tuple(point + delta)]]
        if tuple(-delta) in possible_matches:
            valid_directions.append(delta)
    return valid_directions

valid_directions = find_valid_directions(starting_point)

# Now there are two paths.
# Continue while the current points are not the same
steps = 1
visited_points = [starting_point, *(starting_point + valid_directions)]
# print(visited_points)
path1 = [tuple(starting_point + valid_directions[0])]
path2 = [tuple(starting_point + valid_directions[1])]
current1 = path1[-1]
current2 = path2[-1]
while current1 != current2: # Insert condition
    valid_directions1 = find_valid_directions(current1, np.array(pipe_map[data[current1]]))
    valid_directions2 = find_valid_directions(current2, np.array(pipe_map[data[current2]]))
    valid_points1 = valid_directions1 + np.array(current1)
    valid_points2 = valid_directions2 + np.array(current2)
    for point in valid_points1:
        if tuple(point) not in path1:
            path1.append(tuple(point))
            current1 = path1[-1] 

    for point in valid_points2:
        if tuple(point) not in path2:
            path2.append(tuple(point))
            current2 = path2[-1] 
    
    steps += 1

print("Steps: ", steps)