with open("input.txt") as f:
    round_list = f.readlines()

total_score = 0

moves = {
    "A": 1, # rock
    "B": 2, # paper
    "C": 3, # scissors
    "X": "lose",
    "Y": "tie",
    "Z": "win"
}

for x in round_list:
    opponent = x.split()[0]
    objective = moves.get(x.split()[1])

    if objective == "lose":
        points = moves.get(opponent) - 1

        if points == 0:
            points = 3

        total_score += points
        continue
  
    if objective == "tie":
        total_score += moves.get(opponent) + 3
        continue

    if objective == "win":
        points = moves.get(opponent) + 1

        if points == 4:
            points = 1

        total_score += points + 6
        continue

print(total_score)
