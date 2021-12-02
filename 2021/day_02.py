import pandas as pd

df = pd.read_csv(
    "./input_02.txt",
    delimiter=" ",
    header=None,
)
df.columns = ["command", "value"]
grouped = df.groupby("command").sum()["value"]

depth = grouped["down"] - grouped["up"]
h_pos = grouped["forward"]

print(f"Part 1 answer: {depth * h_pos}")
