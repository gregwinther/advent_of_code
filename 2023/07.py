import re
from collections import Counter

# test_input="""32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483
# """
# 
# lines = test_input.split("\n")[:-1]

with open("./input07.txt") as f:
    lines = f.readlines()

lines = list(map(lambda x: x.replace("\n", ""), lines))

hands, bets = [], []
for line in lines:
    hand, bet = line.split(" ")
    hands.append(hand)
    bets.append(int(bet))

hand_data = []
for hand, bet in zip(hands, bets):
    hand_stats = Counter(hand)

    counts = list(hand_stats.values())
    score = 1
    if 5 in counts:
        score = 7
    elif 4 in counts:
        score = 6
    elif 3 in counts and 2 in counts:
        score = 5
    elif 3 in counts:
        score =  4
    elif counts.count(2) == 2:
        score =  3
    elif 2 in counts:
        score = 2

    hand_data.append((score, *map("*23456789TJQKA".index, hand), bet)) 


sorted_hand_data = sorted(hand_data)

winnings = 0
for rank, (*_, bet) in enumerate(sorted_hand_data):
    winnings += (rank + 1) * bet

print("Winnings: ", winnings)
