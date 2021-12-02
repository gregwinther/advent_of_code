import pandas as pd

# Part 1

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

# Part 2

df["up_down"] = 0
df.loc[df.command == "down", "up_down"] = 1
df.loc[df.command == "up", "up_down"] = -1
df["aim"] = df["value"] * df["up_down"]
df["aim"] = df["aim"].cumsum()
df["h_pos"] = df.loc[
    df.command == "forward", "value"
].cumsum()
df["h_pos"] = df["h_pos"].fillna(method="ffill")
df["v_pos"] = df.loc[
    df.command == "forward", "value"
] * df["aim"]
df["v_pos"] = df["v_pos"].cumsum().fillna(method="ffill")

print(df["h_pos"].iloc[-1] * df["v_pos"].iloc[-1])