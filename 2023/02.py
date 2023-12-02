import re

## Part I

test_data = """Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"""

lines = test_data.split("\n")

# What games would be possible if the bag contained 
# only 12 red cubes, 13 green cubes, and 14 blue cubes?

game_dict = {}
for line in lines:
    game_id = re.search(r"(?<=Game )(\d+)(?=:)", line).group(1)
    game_dict[int(game_id)] = line.split(":")[1]