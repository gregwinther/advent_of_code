# filepath = "./test_input.txt"
filepath = "./input.txt"
with open(filepath, "r") as f:
    lines = f.readlines()

lines = [(line[0], int(line[1:].strip())) for line in lines]

dial = 50
zero_counter = 0

for dir, num in lines:
    if dir == "R":
        zero_counter += (dial + num) // 100
        dial = (dial + num) % 100
    elif dir == "L":
        new_dial = (dial - num) % 100

        # Started at zero
        if dial == 0:
            zero_counter += num // 100
        # Cross zero at least once
        elif num > dial:
            zero_counter += ((num - dial - 1) // 100) + 1
            # Count final if stops on 0
            if new_dial == 0:
                zero_counter += 1
        # Land on 0?
        elif num == dial:
            zero_counter += 1

        # Else: num < dial. zero not reached.

        dial = new_dial

print("Zeros: ", zero_counter) 