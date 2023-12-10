import re
from itertools import cycle

# input_data = """LLR
# 
# AAA = (BBB, BBB)
# BBB = (AAA, ZZZ)
# ZZZ = (ZZZ, ZZZ)"""

# input_data = """LR
# 
# 11A = (11B, XXX)
# 11B = (XXX, 11Z)
# 11Z = (11B, XXX)
# 22A = (22B, XXX)
# 22B = (22C, 22C)
# 22C = (22Z, 22Z)
# 22Z = (22B, 22B)
# XXX = (XXX, XXX)"""

with open("./input08.txt") as f:
    input_data = f.read().strip()

directions, raw = input_data.split("\n\n")

nodes = {}
for line in raw.split("\n"):
    key, left, right = re.findall(r"[\w\d]{3}", line)
    nodes[key] = {"L": left, "R": right}

def solve(position = "AAA", directions=cycle("LR")): 
    for i, dir in enumerate(directions):
        if position[-1] == "Z":
            return i
        position = nodes[position][dir]

## print("Steps: ", solve("AAA")) 

starting_points = [node for node in nodes if node[-1] == "A"]
solns = [solve(node, cycle(directions)) for node in starting_points]

from math import lcm

print("Least common multiplier: ", lcm(*solns))