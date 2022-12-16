with open("input.txt") as f:
    content = f.readline()

# length of substring to find with no repeats
LEN_NO_REPEATS = 14

# finds indexes of substring that don't repeat
def find_no_repeats():
    for x in range(len(content) - LEN_NO_REPEATS - 1):
        substring = content[x:x + LEN_NO_REPEATS]
        # attempts to remove each character in combo from substring
        for i in range(LEN_NO_REPEATS):
            prev_len = len(substring)
            substring = substring.replace(content[x + i], "")

            # if replaced removed more than 1 char, then there is a duplicate
            if len(substring) < prev_len - 1:
                break

            # if all chars in substring are removed without duplicate found, then return end of substring index
            if len(substring) == 0:
                return x + LEN_NO_REPEATS

print(find_no_repeats())