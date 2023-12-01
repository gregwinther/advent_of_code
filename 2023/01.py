import re

with open("./input01.txt") as f:
	lines = f.readlines()

## Part I

# test_input = """1abc2
# pqr3stu8vwx
# a1b2c3d4e5f
# treb7uchet"""
# 
# lines = test_input.split("\n")

calibration_numbers = []
for line in lines:
	res = re.findall(r"\d", line)

	if len(res) > 1:
		calibration_numbers.append(res[0] + res[-1])
	else:
		calibration_numbers.append(res[0] + res[0])

calibration_numbers = list(map(int, calibration_numbers))

print("Sum of calibration numbers, part I:  ", sum(calibration_numbers))

## Part II

# test_input = """two1nine
# eightwothree
# abcone2threexyz
# xtwone3four
# 4nineeightseven2
# zoneight234
# 7pqrstsixteen"""
# 
# lines = test_input.split("\n")

calibration_numbers = []
for line in lines:
	res_ = re.findall(r"(?=(\d|one|two|three|four|five|six|seven|eight|nine))", line)

	res = []
	for dig in res_:
		if dig == "one":
			res.append("1")
		elif dig == "two":
			res.append("2")
		elif dig == "three":
			res.append("3")	
		elif dig == "four":
			res.append("4")
		elif dig == "five":
			res.append("5")
		elif dig == "six":
			res.append("6")
		elif dig == "seven":
			res.append("7")
		elif dig == "eight":
			res.append("8")
		elif dig == "nine":
			res.append("9")
		else:
			res.append(dig)
	
	if len(res) > 1:
		calibration_numbers.append(res[0] + res[-1])
	else:
		calibration_numbers.append(res[0] + res[0])


calibration_numbers = list(map(int, calibration_numbers))

print("Sum of calibration numbers, part II: ", sum(calibration_numbers))


