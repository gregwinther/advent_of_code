import re
from itertools import cycle

# input_data = """LLR
# 
# AAA = (BBB, BBB)
# BBB = (AAA, ZZZ)
# ZZZ = (ZZZ, ZZZ)"""

with open("./input08.txt") as f:
    input_data = f.read().strip()

directions, raw = input_data.split("\n\n")

nodes = {}
for line in raw.split("\n"):
    key, left, right = re.findall(r"\w{3}", line)
    nodes[key] = {"L": left, "R": right}

directions = cycle(directions) # Amazing trick!!

def solve(position = "AAA"): 
    for i, dir in enumerate(directions):
        if position[-1] == "Z":
            return i
        position = nodes[position][dir]

print("Steps: ", solve("AAA"))
