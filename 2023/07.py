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

hand_type = []
card_values = []
for hand in hands:
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

    hand_type.append(score)
    card_values.append(list(map("*23456789TJQKA".index, hand)))

scores = [(ht, cv) for ht, cv in zip(hand_type, card_values)]
sorted_scores = sorted(enumerate(scores), key=lambda x: x[1])
ranks = [i + 1 for i, _ in sorted_scores]

winnings = 0
for rank, bet in zip(ranks, bets):
    winnings += rank * bet

print("Total winnings: ", winnings)