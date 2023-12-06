import re
from math import prod

# test_input="""Time:      7  15   30
# Distance:  9  40  200
# """
# 
# lines = test_input.split("\n")[:-1]

actual_input = """Time:        35     93     73     66
Distance:   212   2060   1201   1044
"""

lines = actual_input.split("\n")[:-1]

race_times = list(map(int, re.findall(r"\d+", lines[0])))
distances = list(map(int, re.findall(r"\d+", lines[1])))

button_hold_times = []
for time, dist in zip(race_times, distances):
    race_button_hold_times = [] 
    for button_hold_time in range(1, dist + 1):
        speed = button_hold_time
        time_left = time - button_hold_time
        distance_travelled = speed * time_left
        if distance_travelled > dist:
            race_button_hold_times.append(button_hold_time)
    button_hold_times.append(race_button_hold_times)

ways_to_beat_race = [len(bht) for bht in button_hold_times]

print("Product of ways to beat race:", prod(ways_to_beat_race))

## Part II

# Test data
race_time = 71530
distance = 940200

# Actual data
race_time = 35937366
distance = 212206012011044

def compute_distance(hold_time, race_time):
    speed = hold_time
    time_left = race_time - hold_time
    distance_travelled = speed * time_left
    return distance_travelled

# lowest time to hold button
for hold_time in range(race_time):
    distance_travelled = compute_distance(hold_time, race_time) 
    if distance_travelled > distance:
        low_hold_time = hold_time
        break

# longest time to hold button
for hold_time in range(race_time, 0, -1):
    distance_travelled = compute_distance(hold_time, race_time)
    if distance_travelled > distance:
        high_hold_time = hold_time
        break

print("Ways to beat the record: ", high_hold_time - low_hold_time + 1)