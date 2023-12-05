import re

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
        
        maps[map_name] = []
        for k in range (i + 1, map_end + 1):
            dest, source, range_len = re.findall(r"\d+", lines[k])
            dest, source, range_len = int(dest), int(source), int(range_len)
            maps[map_name].append({k: v for k, v in zip(range(source, source + range_len), range(dest, dest + range_len))})

# Merge the dicts in the maps
for map_name in maps:
    merged_dict = {}
    for d in maps[map_name]:
        for k, v in d.items():
            merged_dict[k] = v
    maps[map_name] = merged_dict

# Note: Any source numbers that aren't mapped correspond to the same destination number.

location_numbers = []
for seed in seeds:
    if seed not in maps["seed-to-soil"]:
        soil = seed
    else:
        soil = maps["seed-to-soil"][seed]

    if soil not in maps["soil-to-fertilizer"]:
        fertilizer = soil
    else:
        fertilizer = maps["soil-to-fertilizer"][soil]

    if fertilizer not in maps["fertilizer-to-water"]:
        water = fertilizer
    else:
        water = maps["fertilizer-to-water"][fertilizer]
    
    if water not in maps["water-to-light"]:
        light = water
    else:
        light = maps["water-to-light"][water]

    if light not in maps["light-to-temperature"]:
        temperature = light
    else:
        temperature = maps["light-to-temperature"][light]

    if temperature not in maps["temperature-to-humidity"]:
        humidity = temperature
    else:
        humidity = maps["temperature-to-humidity"][temperature]

    if humidity not in maps["humidity-to-location"]:
        location = humidity
    else:
        location = maps["humidity-to-location"][humidity]

    # print(seed, soil, fertilizer, water, light, temperature, humidity, location)

    location_numbers.append(location)

print("Lowest location number: ", min(location_numbers))