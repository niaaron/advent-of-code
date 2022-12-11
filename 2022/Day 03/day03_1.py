with open("input.txt") as f:
    contents = f.readlines()

recurring_letters = []

for bag in contents:
    comp_one = bag[:int((len(bag) - 1)/2)]
    comp_two = bag[int((len(bag) - 1)/2):]
    
    for comp_one_letter in comp_one:
        if comp_one_letter in comp_two:
            recurring_letters.append(comp_one_letter)
            break

priorities_sum = 0

for letter in recurring_letters:
    if letter.islower():
        priorities_sum += ord(letter) - 96
    else:
        priorities_sum += ord(letter) - 38

print(priorities_sum)
