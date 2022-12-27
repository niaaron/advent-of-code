with open("Day 08/input.txt") as f:
    contents = f.read().splitlines() 

# returns the number of trees visible in each direction from current tree multiplied together
def get_scenic_score(y, x):
    tree_height = contents[y][x]
    
    # checks trees on top
    top_score = 0
    for i in range(1, y + 1):
        top_score += 1
        if contents[y - i][x] >= tree_height:
            break

    # checks trees on bottom
    bottom_score = 0
    for i in range(1, len(contents) - y):
        bottom_score += 1
        if contents[y + i][x] >= tree_height:
            break

    # checks trees on left
    left_score = 0
    for i in range(1, x + 1):
        left_score += 1
        if contents[y][x - i] >= tree_height:
            break

    # checks trees on right
    right_score = 0
    for i in range(1, len(contents) - x):
        right_score += 1
        if contents[y][x + i] >= tree_height:
            break

    
    return top_score * bottom_score * left_score * right_score

# contains scores of all tree (starts with a 0 to represent border trees)
scenic_scores = [0]

# loops through all inner trees
for y in range(1, len(contents) - 1):
    for x in range(1, len(contents[y]) - 1):
        scenic_scores.append(get_scenic_score(y, x))

print(max(scenic_scores))