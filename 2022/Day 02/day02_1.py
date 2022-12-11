with open("input.txt") as f:
    round_list = f.readlines()

total_score = 0

moves = {
    "A": 1, # rock
    "B": 2, # paper
    "C": 3, # scissors
    "X": 1, # rock
    "Y": 2, # paper
    "Z": 3  # scissors
}

for x in round_list:
    opponent = x.split()[0]
    you = x.split()[1]

    # tie
    if moves.get(you) == moves.get(opponent):
        total_score += moves.get(you) + 3
        continue

    # you choose scissor and they choose rock
    if moves.get(you) == 3 and moves.get(opponent) == 1:
        # lose
        total_score += moves.get(you)
        continue

    # you choose rock and they choose scissors
    if moves.get(you) == 1 and moves.get(opponent) == 3 or moves.get(you) > moves.get(opponent):
        # win
        total_score += moves.get(you) + 6
    else:
        # lose
        total_score += moves.get(you)

print(total_score)
