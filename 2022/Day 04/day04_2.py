with open("input.txt") as f:
    contents = f.readlines()

overlap_count = 0

for pairs in contents:
    pair_one = list(map(int, pairs.split(",")[0].split("-")))
    pair_two = list(map(int, pairs.split(",")[1].split("-")))

    if pair_one[0] > pair_two[1] or pair_two[0] > pair_one[1]:
        continue

    overlap_count += 1

print(overlap_count)