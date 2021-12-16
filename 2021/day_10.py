# Part 1

test_data = [
    "[({(<(())[]>[[{[]{<()<>>",
    "[(()[<>])]({[<{<<[]>>(",
    "{([(<{}[<>[]}>{[]{[(<()>",
    "(((({<>}<{<{<>}{[]{[]{}",
    "[[<[([]))<([[{}[[()]]]",
    "[{[{({}]{}}([{[{{{}}([]",
    "{<[[]]>}<{[{[{[]{()[[[]",
    "[<(<(<(<{}))><([]([]()",
    "<{([([[(<>()){}]>(<<{{",
    "<{([{{}}[<[[[<>{}]]]>[]]",
]

data = test_data

start_brackets = "{([<"
stop_brackets = "})]>"

# Make map of corresponding opening, closing brackets
start_bracket_dict = {
    start: stop for start, stop in zip(start_brackets, stop_brackets)
}
stop_bracket_dict = {
    stop: start for start, stop in zip(start_brackets, stop_brackets)
}

syntax_error_scores = {")": 3, "]": 57, "}": 1197, ">": 25137}


# An exercise in ones knowledge of the stack data structure
def string_searcher(string):
    stack = []
    for ch in string:
        if ch in start_brackets:
            stack.append(ch)
        elif ch in stop_brackets:  # End of start. Removing from stack.
            popped = stack.pop()
            if stop_bracket_dict[ch] != popped:  # Match?
                print(f"Expected {start_bracket_dict[popped]}, found {ch}")


for i, line in enumerate(data):
    string_searcher(line)
