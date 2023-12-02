# readlines function
# 1. find the element occurs in each half in every line
# 2. priority: a-z + A-Z zip dictionary 1-52
# 3. sum of priorities of those item types.

with open("Day 3\input.txt") as file:
    file_contents = [item.strip("\n") for item in file.readlines()]

    halved_contents = []
    for str in file_contents:
        splitted_string = []
        first_half, second_half = str[:len(str)//2], str[len(str)//2:]
        splitted_string.append(first_half)
        splitted_string.append(second_half)
        halved_contents.append(splitted_string)

    print(halved_contents)

    

    