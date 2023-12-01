with open("input.txt") as f:
    calibration_doc = f.readlines()

sum = 0

for line in calibration_doc:
    calibration_values = ""
    for char in line:
        if char.isnumeric():
            calibration_values += char
            break

    for char in line[::-1]:
        if char.isnumeric():
            calibration_values += char
            break

    sum += int(calibration_values)

print(sum)

