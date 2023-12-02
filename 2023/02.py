import re

## Part I

# test_data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
# Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
# Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
# Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
# Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""
# 
# lines = test_data.split("\n")

with open("./input02.txt") as f:
    lines = f.readlines()

# What games would be possible if the bag contained 
# only 12 red cubes, 13 green cubes, and 14 blue cubes?

game_dict = {}
for line in lines:
    game_id = re.search(r"(?<=Game )(\d+)(?=:)", line).group(1)
    game_dict[int(game_id)] = line.split(":")[1]

max_cube_counts = {}
for id, gamespecs in game_dict.items():
    games = gamespecs.split(";")
    # Find green, blue, red
    green, blue, red = [], [], []
    for game in games:
        blue_search = re.search(r"(\d+)( blue)", game)
        if blue_search:
            blue.append(blue_search.group(1))
        green_search = re.search(r"(\d+)( green)", game)
        if green_search:
            green.append(green_search.group(1))
        red_search = re.search(r"(\d+)( red)", game)
        if red_search:
            red.append(red_search.group(1))

    blue = list(map(int, blue))
    green = list(map(int, green))
    red = list(map(int, red))

    max_cube_counts[id] = {
        "blue": max(blue),
        "green": max(green),
        "red": max(red),
    }


# What games would be possible if the bag contained 
# only 12 red cubes, 13 green cubes, and 14 blue cubes?

game_criteria = {
    "red": 12,
    "green": 13,
    "blue": 14
}

allowed_games = []
for id, max_val_dict in max_cube_counts.items():
    if not (
        game_criteria["red"] < max_val_dict["red"] or
        game_criteria["green"] < max_val_dict["green"] or
        game_criteria["blue"] < max_val_dict["blue"]
    ):
        allowed_games.append(id)

print("Sum of allowed games: ", sum(allowed_games))