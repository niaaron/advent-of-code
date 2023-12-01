def check_if_number(curr_index, string):
    three_char = string[curr_index:curr_index + 3]
    four_char = string[curr_index:curr_index + 4]
    five_char = string[curr_index:curr_index + 5]

    if three_char == "one":
        return 1

    if three_char == "two":
        return 2

    if five_char == "three":
        return 3

    if four_char == "four":
        return 4

    if four_char == "five":
        return 5

    if three_char == "six":
        return 6

    if five_char == "seven":
        return 7

    if five_char == "eight":
        return 8

    if four_char == "nine":
        return 9

    return -1

with open("input.txt") as f:
    calibration_doc = f.readlines()

sum = 0

for line in calibration_doc:
    calibration_values = ""
    for x in range(len(line)):
        num_check = check_if_number(x, line)
        if num_check != -1:
            calibration_values += str(num_check)
            break

        if line[x].isnumeric():
            calibration_values += line[x]
            break

    for x in reversed(range(len(line))):
        num_check = check_if_number(x, line)
        if num_check != -1:
            calibration_values += str(num_check)
            break

        if line[x].isnumeric():
            calibration_values += line[x]
            break

    sum += int(calibration_values)

print(sum)

