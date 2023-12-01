import fileinput
import re

DIGITS = {
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

total = 0
for line in fileinput.input():
    sub_line = line
    for digit, d in DIGITS.items():
        sub_line = re.sub(digit, digit + str(d) + digit, sub_line)
    digits = [char for char in sub_line if char.isdigit()]
    if digits:
        print(int(digits[0] + digits[-1]))
        total += int(digits[0] + digits[-1])
print(total)
