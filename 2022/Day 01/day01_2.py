with open("input.txt") as f:
    calorie_list = f.readlines()

calorie_sums = []
current_sum = 0

for x in calorie_list:
    if x != "\n":
        current_sum += int(x)
    else:
        calorie_sums.append(current_sum)
        current_sum = 0

top_three_total = 0

for x in range(3):
    most_calories = max(calorie_sums)
    top_three_total += most_calories
    calorie_sums.remove(most_calories)

print(top_three_total)
