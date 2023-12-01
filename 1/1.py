import fileinput

total = 0
for line in fileinput.input():
    digits = [char for char in line if char.isdigit()]
    if digits:
        total += int(digits[0] + digits[-1])
print(total)
