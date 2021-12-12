from collections import Counter
from os import uname

with open("./input_08.txt", "r") as f:
    data = f.read().splitlines()

# Test data
# data = [
#     "be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe",
#     "edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc",
#     "fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg",
#     "fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb",
#     "aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea",
#     "fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb",
#     "dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe",
#     "bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef",
#     "egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb",
#     "gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce",
# ]

data = list(map(lambda str: str.split(" | "), data))

digit_count_map = {
    2: 1,
    4: 4,
    3: 7,
    7: 8,
}
digit_counts = dict.fromkeys(digit_count_map.keys(), 0)
for in_out in data:
    _, output = in_out

    out_digits = output.split(" ")

    for digit in out_digits:
        n = len(digit)
        if n in digit_counts:
            digit_counts[n] += 1

# print(digit_counts)
print(f"Number of times 1, 4, 7, 8 appears: {sum(digit_counts.values())}")

# PART 2
## The frequency of characters in combination with the number of fields lit up
## and lenght of string should be unique.
## Get numeric representation for count of letters.


def get_char_frequencies(char_counts, number_config):
    frequencies = [str(char_counts[char]) for char in number_config]
    frequencies.sort()  # Surprisingly important
    return int("".join(frequencies))


# Get unique 'ids' for each wiring
correct_wiring_config = (
    "abcefg cf acdeg acdfg bcdf abdfg abdefg acf abcdefg abcdfg"
)
char_counts = Counter(correct_wiring_config.replace(" ", ""))
digits_wire_map = {}
for i, number_config in enumerate(correct_wiring_config.split(" ")):
    unique_representation = get_char_frequencies(
        char_counts, number_config
    )
    # print(i, unique_representation)
    digits_wire_map[unique_representation] = i

# The strings are not always in the same order..
def sort_string(string):
    return str("".join(sorted(string)))


output_values = []
for input, output in data:
    char_counts = Counter(input.replace(" ", ""))
    config_to_number = {}
    for number_config in input.split(" "):
        unique_representation = get_char_frequencies(
            char_counts, number_config
        )
        config_to_number[sort_string(number_config)] = digits_wire_map[
            unique_representation
        ]

    output_values.append(
        int(
            "".join(
                [
                    str(config_to_number[sort_string(config)])
                    for config in output.split(" ")
                ]
            )
        )
    )

print(f"Sum of all outputs: {sum(output_values)}")
