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