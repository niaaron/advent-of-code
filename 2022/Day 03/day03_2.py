with open("input.txt") as f:
    contents = f.readlines()

badges = []

# finds the common letter in the current and next two rucksacks
# then increments to the next set of three
for x in range(0, len(contents), 3): 
    for letter in contents[x]:
        if letter in contents[x+1] and letter in contents[x+2]:
            badges.append(letter)
            break

# calculates priorities of the recurring letters
# a through z have priorities 1 through 26
# A through Z have priorities 27 through 52
priorities_sum = 0

for letter in badges:
    if letter.islower():
        priorities_sum += ord(letter) - 96
    else:
        priorities_sum += ord(letter) - 38

print(priorities_sum)
