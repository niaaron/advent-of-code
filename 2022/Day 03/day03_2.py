with open("input.txt") as f:
    contents = f.readlines()

badges = []

for x in range(0, len(contents), 3): 
    for letter in contents[x]:
        if letter in contents[x+1] and letter in contents[x+2]:
            badges.append(letter)
            break

priorities_sum = 0

for letter in badges:
    if letter.islower():
        priorities_sum += ord(letter) - 96
    else:
        priorities_sum += ord(letter) - 38

print(priorities_sum)
