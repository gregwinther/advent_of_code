# Part 1

with open("./input_01.txt") as f:
    input_strings = f.readlines()

data = []
for string in input_strings:
    data.append(int(string.rstrip("\n")))

n = len(input_strings)
increased = [0] * n
for i in range(1, n):
    if data[i - 1] < data[i]:
        increased[i] = 1

print(f"{sum(increased)} measurements are larger than the previous.")

# Part 2: Three measurement sliding window

three_measurements_sum = []
for i in range(3, n+1):
    three_measurements_sum.append(sum(data[i-3:i]))

m = len(three_measurements_sum)
increased_three = [0] * m
for i in range(1, m):
    if three_measurements_sum[i - 1] < three_measurements_sum[i]:
        increased_three[i] = 1

print(f"Number of increases in windows of 3: {sum(increased_three)}")