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


def find_id_matches(id_ranges, num_matches=2):
    match_counter = 0
    correct_ids = []

    matching_string = r"(\d+)\1{" + str(num_matches-1) + "}"

    for a, b in id_ranges:
        for id in range(int(a), int(b)+1):
            # result = re.findall(r"(\d+)\1", str(id))
            result = re.findall(matching_string, str(id))
            if len(result) > 0:
                first_res = result[0]
                if len(first_res)*num_matches == len(str(id)):
                    match_counter += 1
                    correct_ids.append(int(id))

    return correct_ids, match_counter

valid_ids = []
for i in range(10, 2-1, -1):
    print("Finding matches:", i)
    correct_ids, _ = find_id_matches(id_ranges, num_matches=i) 
    # print("Correct: ", correct_ids)
    # print("n matches: ", n)
    for id in correct_ids:
        valid_ids.append(id)

# print("Valid ids:", valid_ids)
print("Sum of unique:", sum(set(valid_ids)))