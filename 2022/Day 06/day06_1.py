with open("input.txt") as f:
    content = f.readline()

# finds indexes of substring that don't repeat
def find_no_repeats():
    # loops through each combo of 4 chars
    for x in range(len(content) - 3):
        substring = content[x:x + 4]
        # attempts to remove each character in combo from substring
        for i in range(4):
            prev_len = len(substring)
            substring = substring.replace(content[x + i], "")

            # if replaced removed more than 1 char, then there is a duplicate
            if len(substring) < prev_len - 1:
                break
            
            # if all chars in substring are removed without duplicate found, then return end of substring index
            if len(substring) == 0:
                return x + 4

print(find_no_repeats())