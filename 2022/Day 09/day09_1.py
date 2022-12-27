import math

with open("input.txt") as f:
    commands = f.read().splitlines() 

ROPE_LENGTH = 1

head_pos = (0,0)
tail_pos = (0,0)

# distance formula between two points floored (turned to int)
def distance_between(pos_one, pos_two):
    return int(math.sqrt((pos_two[0] - pos_one[0]) ** 2 + (pos_two[1] - pos_one[1]) ** 2))

# parses command's direction; returns tuple with the direction and magnitude to be moved
def move_distance(direction):
    if direction == "U":
        return (0, 1)
    elif direction == "D":
        return (0, -1)
    elif direction == "L":
        return (-1, 0)
    elif direction == "R":
        return (1, 0)
    else:
        print("That ain't a direction!")

# stores the positions the tail has been in a set to prevent duplicates
past_tail_pos = {(0,0)}

# loops through each command given
for command in commands:
    # a tuple with how many spots to move (+/-)
    move = move_distance(command.split()[0])
    # loops command for number of times specified
    for repeats in range(int(command.split()[1])):
        # stores past head position to move tail too if needed
        old_head_pos = head_pos

        # moves head
        head_pos = (head_pos[0] + move[0], head_pos[1] + move[1])
        
        # checks if distance between head an tail is longer than the rope and moves tail
        if distance_between(tail_pos, head_pos) > ROPE_LENGTH:
            tail_pos = old_head_pos

            # adds position to tail's position history
            past_tail_pos.add(tail_pos)

print(len(past_tail_pos))