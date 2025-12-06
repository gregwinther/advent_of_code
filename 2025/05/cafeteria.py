# file_path = "./test_input.txt"
file_path = "./input.txt"

with open(file_path, "r") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]

id_ranges = []
empty_line_found = False
ingredients = []
for line in lines:
    if line == "":
        empty_line_found = True
        continue
    if not empty_line_found:
        start, stop = map(int, line.split("-"))
        id_ranges.append((start, stop))
    else:
        ingredients.append(int(line))

fresh_ingredients = set()
for ingredient in ingredients:
    for start, stop in id_ranges:
        if start <= ingredient <= stop:
            fresh_ingredients.add(ingredient)
            break

print("No of valid ingredients:", len(list(fresh_ingredients)))

# Part 2: How many numbers are in the ranges (inclusive)?
# Merge overlapping ranges and count unique numbers
id_ranges.sort() # This works!!! ??!?
merged_ranges = []
for start, stop in id_ranges:
    # None yet or no overlap
    if not merged_ranges or merged_ranges[-1][1] < start - 1:
        merged_ranges.append([start, stop])
    else:
        merged_ranges[-1][1] = max(merged_ranges[-1][1], stop)
total_count = 0
for start, stop in merged_ranges:
    total_count += (stop - start + 1)

print("Total number of valid ingredients:", total_count)