# filepath = "./test_input.txt"
filepath = "./input.txt"
with open(filepath, "r") as f:
    lines = f.readlines()

lines = [(line[0], int(line[1:].strip())) for line in lines]

# print(lines)

dial = 50
zero_counter = 0
# print(dial)

for dir, num in lines:
    if dir == "R":
        dial += num
    elif dir == "L":
        dial -= num

    if dial < 0:
        dial = 100 + dial

    dial = dial % 100
    
    if dial == 0:
        zero_counter += 1

    # print(dir, num, dial)
print("Zeros: ", zero_counter) 