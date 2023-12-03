import re
import pandas as pd

## Part I

# test_data = """467..114..
# ...*......
# ..35..633.
# ......#...
# 617*......
# .....+.58.
# ..592.....
# ......755.
# ...$.*....
# .664.598.."""
# 
# lines = test_data.split("\n")

with open("./input03.txt") as f:
    lines = f.readlines()

    matrix = []
for line in lines:
    matrix.append(list(line))

directions = [
    [-1, -1], [-1, 0], [-1, 1], [0, -1], [0, 1], [1, -1], [1, 0], [1, 1]
]

N = len(matrix[0]) # Width (x-axis)
M = len(matrix) # Height 

numbers = []
number_coords = []
for y in range(M):
    for x in range(N):
        symbol = matrix[y][x]
        # Not a digit, not "." 
        if re.match("\D", symbol) and symbol != ".":

            prev_number_start_index = 0
            prev_number_end_index = 0
            prev_check_y = 0

            # Check in all directions for numbers
            for dir in directions:
                dx, dy = dir
                check_x, check_y = x + dx, y + dy

                # Don't check for same again.
                if check_y == prev_check_y and prev_number_start_index <= check_x <= prev_number_end_index:
                    continue

                # Make sure we are not checking outside of matrix
                if 0 <= check_x < N and 0 <= check_y < M:
                    check_symbol = matrix[check_y][check_x]

                    # is digit?
                    if re.match(r"\d", check_symbol):
                        ## Look for full number
                        
                        # Find start
                        number_start_index = check_x
                        while number_start_index > 0:
                            if re.match(r"\d", matrix[check_y][number_start_index - 1]):
                                number_start_index -= 1
                            else:
                                break

                        # Find end
                        number_end_index = check_x
                        while number_end_index < N - 1:
                            if re.match(r"\d", matrix[check_y][number_end_index + 1]):
                                number_end_index += 1
                            else:
                                break

                        prev_number_start_index = number_start_index
                        prev_number_end_index = number_end_index
                        prev_check_y = check_y

                        number = int("".join(matrix[check_y][number_start_index:number_end_index + 1]))
                        
                        numbers.append(number)
                        number_coords.append(f"{number_start_index}_{check_y}")

# I count some things several time..
df = pd.DataFrame({"coords": number_coords, "number": numbers})

print("Sum of numbers: ", df.drop_duplicates(subset="coords")["number"].sum())