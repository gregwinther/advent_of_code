import re

# filepath = "./test_input.txt"
filepath = "./input.txt"

with open(filepath, "r") as f:
    lines = f.readlines()

lines = [line.strip() for line in lines]
line = ""
for l in lines:
    line += l
id_ranges = line.split(",")
id_ranges = [id_range.split("-") for id_range in id_ranges]

match_counter = 0
correct_ids = []

for a, b in id_ranges:
    # print(a, b)

    for id in range(int(a), int(b)+1):
        result = re.findall(r"(\d+)\1", str(id))

        if len(result) > 0:
            first_res = result[0]
            if len(first_res)*2 == len(str(id)):
                # print("  ", id)
                # print("  ", first_res)
                match_counter += 1
                correct_ids.append(int(id))

print("Correct ids: ", match_counter)
print("Sum of correct ids: ", sum(correct_ids))
# print(correct_ids)