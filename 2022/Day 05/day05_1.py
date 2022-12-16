with open("input.txt") as f:
    contents = f.readlines()

stacks = []

# converts input diagram stacks into arrays
def parse_stacks():
    rows = []
    for line in contents:
        # checks that current line is part of diagram
        if line[0] != "[":
            break

        row = []
        # increments by 4 to select contents in diagram
        for x in range(1, len(line) - 1, 4):
            row.append(line[x])

        rows.append(row)

    # formats extracted rows into correct stacks
    # loops through the number of stacks in input
    for i in range(len(rows[0])):
        stack = []

        # gets i (stack) by combining i-th value from each extracted row
        for row in rows:
            if row[i] != " ":
                stack.append(row[i])
        
        stack.reverse()
        stacks.append(stack)

# moves items from one stack to another stack
def move(amount, start_stack, end_stack):
    for _ in range(amount):
        crate = stacks[start_stack - 1].pop()
        stacks[end_stack - 1].append(crate)

def main():
    parse_stacks()

    # loops through each move direction
    for line in contents:
        # checks that current line is part of the directions
        if line[0] != "m":
            continue

        # extracts move directions
        amount = int(line.split(" ")[1])
        start_stack = int(line.split(" ")[3])
        end_stack = int(line.split(" ")[5])

        move(amount, start_stack, end_stack)

    # prints the top value of each stack
    for stack in stacks:
        print(stack.pop(), end=""),

main()