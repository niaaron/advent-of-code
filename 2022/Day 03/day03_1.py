with open("input.txt") as f:
    contents = f.readlines()

recurring_letters = []

for bag in contents:
    # splits bags up into two even compartments
    comp_one = bag[:int((len(bag) - 1)/2)]
    comp_two = bag[int((len(bag) - 1)/2):]
    
    # checks if letter in one compartment shows up in the other
    for comp_one_letter in comp_one:
        if comp_one_letter in comp_two:
            recurring_letters.append(comp_one_letter)
            break

# calculates priorities of the recurring letters
# a through z have priorities 1 through 26
# A through Z have priorities 27 through 52
priorities_sum = 0

for letter in recurring_letters:
    if letter.islower():
        priorities_sum += ord(letter) - 96
    else:
        priorities_sum += ord(letter) - 38

print(priorities_sum)
