with open("input.txt") as f:
    contents = f.readlines()

fully_contains_count = 0

for pairs in contents:
    pair_one = list(map(int, pairs.split(",")[0].split("-")))
    pair_two = list(map(int, pairs.split(",")[1].split("-")))

    if pair_one[1] - pair_one[0] > pair_two[1] - pair_two[0]:
        if pair_one[1] >= pair_two[1] and pair_one[0] <= pair_two[0]:
            fully_contains_count += 1
    else:
        if pair_two[1] >= pair_one[1] and pair_two[0] <= pair_one[0]:
            fully_contains_count += 1

print(fully_contains_count)