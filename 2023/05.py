import re
from typing import Any

# test_input = """seeds: 79 14 55 13
# 
# seed-to-soil map:
# 50 98 2
# 52 50 48
# 
# soil-to-fertilizer map:
# 0 15 37
# 37 52 2
# 39 0 15
# 
# fertilizer-to-water map:
# 49 53 8
# 0 11 42
# 42 0 7
# 57 7 4
# 
# water-to-light map:
# 88 18 7
# 18 25 70
# 
# light-to-temperature map:
# 45 77 23
# 81 45 19
# 68 64 13
# 
# temperature-to-humidity map:
# 0 69 1
# 1 0 69
# 
# humidity-to-location map:
# 60 56 37
# 56 93 4
# """
# 
# lines = test_input.split("\n")[:-1]

with open("./input05.txt") as f:
    lines = f.readlines()
lines = list(map(lambda x: x.replace("\n", ""), lines))

class AlmanacMap():

    def __init__(self) -> None:
        self.source = []
        self.dest = []
        self.range_len = []

    def add_map(self, dest, source, range_len):
        self.source.append(source)
        self.dest.append(dest)
        self.range_len.append(range_len)

    def __call__(self, n) -> Any:
        for s, d, r in zip(self.source, self.dest, self.range_len):
            if n in range(s, s + r):
                return d + (n - s)
        else:
            return n
        
    def backwards(self, n) -> int:
        for s, d, r in zip(self.source, self.dest, self.range_len):
            if n in range(d, d + r):
                return s + (n - d)
        else:
            return n
 

# Part One
seeds = list(map(int, lines[0].split(" ")[1:]))

n = len(lines)
maps = {}
for i, line in enumerate(lines):
    # Get map name 
    if re.match("\D+", line) and "seeds" not in line:
        # Find end of map
        map_name = line.replace(" map:", "") 
        for j in range(i, n):
            map_end = j
            if len(lines[j]) <= 1:
                map_end = j - 1
                break
        maps[map_name] = AlmanacMap()
        for k in range (i + 1, map_end + 1):
            dest, source, range_len = re.findall(r"\d+", lines[k])
            dest, source, range_len = int(dest), int(source), int(range_len)
            maps[map_name].add_map(dest, source, range_len)

location_numbers = []
for seed in seeds:
    soil = maps["seed-to-soil"](seed)
    fertilizer = maps["soil-to-fertilizer"](soil)
    water = maps["fertilizer-to-water"](fertilizer)
    light = maps["water-to-light"](water)
    temperature = maps["light-to-temperature"](light)
    humidity = maps["temperature-to-humidity"](temperature)
    location = maps["humidity-to-location"](humidity)

    location_numbers.append(location)

print("Lowest location number: ", min(location_numbers))

## Part Two

def find_seed_number(location):
    humidity = maps["humidity-to-location"].backwards(location)
    temperature = maps["temperature-to-humidity"].backwards(humidity)
    light = maps["light-to-temperature"].backwards(temperature)
    water = maps["water-to-light"].backwards(light)
    fertilizer = maps["fertilizer-to-water"].backwards(water)
    soil = maps["soil-to-fertilizer"].backwards(fertilizer)
    seed = maps["seed-to-soil"].backwards(soil)

    return seed

def is_valid_seed(soil):
    for i in range(0, len(seeds), 2):
        if seeds[i] <= soil < seeds[i] + seeds[i+1]:
            return True
    return False

# Start at zero. Stop when finding a valid seed number
location_number = -1
valid_seed = False 
while not valid_seed:
    location_number += 1 
    seed = find_seed_number(location_number)
    print(location_number, end="\r")
    valid_seed = is_valid_seed(seed)

print("Lowest location number corresponding to valid seed: ", location_number)