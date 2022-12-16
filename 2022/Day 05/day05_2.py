with open("input.txt") as f:
    contents = f.readlines()

stacks = []

def parse_stacks():
    rows = []
    for line in contents:
        if line[0] != "[":
            break

        row = []
        for x in range(1, len(line) - 1, 4):
            row.append(line[x])

        rows.append(row)

    for i in range(len(rows[0])):
        stack = []
        for row in rows:
            if row[i] != " ":
                stack.append(row[i])
        
        stack.reverse()
        stacks.append(stack)

def move(amount, start_stack, end_stack):
    if (amount > 1):
        stack_to_move = []
        for _ in range(amount):
            stack_to_move.append(stacks[start_stack - 1].pop())
        
        stack_to_move.reverse()

        for crate in stack_to_move:
            stacks[end_stack - 1].append(crate)
    else:
        for _ in range(amount):
            crate = stacks[start_stack - 1].pop()
            stacks[end_stack - 1].append(crate)

def main():
    parse_stacks()

    for line in contents:
        if line[0] != "m":
            continue

        amount = int(line.split(" ")[1])
        start_stack = int(line.split(" ")[3])
        end_stack = int(line.split(" ")[5])

        move(amount, start_stack, end_stack)

    for stack in stacks:
        print(stack.pop(), end="")

main()