with open("input.txt") as f:
    contents = f.read().splitlines() 

# returns if a tree at specified coord is visible from the border or not
def is_visible(y, x):
    tree_height = contents[y][x]
    
    # checks trees on top
    top_visible = True
    for i in range(1, y + 1):
        if contents[y - i][x] >= tree_height:
            top_visible = False

    if top_visible:
        return True

    # checks trees on bottom
    bottom_visible = True
    for i in range(1, len(contents) - y):
        if contents[y + i][x] >= tree_height:
            bottom_visible = False

    if bottom_visible:
        return True

    # checks trees on left
    left_visible = True
    for i in range(1, x + 1):
        if contents[y][x - i] >= tree_height:
            left_visible = False

    if left_visible:
        return True

    # checks trees on right
    right_visible = True
    for i in range(1, len(contents) - x):
        if contents[y][x + i] >= tree_height:
            right_visible = False
    
    if right_visible:
        return True
    
    return False

# gets initial number of trees on border since all border trees are visible from border
#                    v left/right border v top/bottom border    v overlapping corners
num_suitable_trees = len(contents) * 2 + len(contents[0]) * 2 - 4

# loops through all inner trees
for y in range(1, len(contents) - 1):
    for x in range(1, len(contents[y]) - 1):
        if is_visible(y, x):
            num_suitable_trees += 1

print(num_suitable_trees)