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