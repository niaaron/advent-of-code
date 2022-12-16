with open("input.txt") as f:
    calorie_list = f.readlines()

most_calories = 0
current_sum = 0

for x in calorie_list:
    if x != "\n":
        current_sum += int(x)
    else:
        if current_sum > most_calories:
            most_calories = current_sum
        current_sum = 0

print(most_calories)
