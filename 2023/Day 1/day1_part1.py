import re

with open("input.txt") as data:
    lines = []

    file_contents = data.readlines()
    for line in file_contents:
        lines.append(line)

    lines = [line.strip("\n") for line in lines] # each list element contains separate line

    # strip the characters
    for i in range(len(lines)):
        filtered = re.sub("[^0-9]", "", lines[i])
        lines[i] = filtered

    #make each string only contain two or one chracters
    for i in range(len(lines)):
        current = lines[i]
        if len(current) > 1: # only for lines with more than 1 chracters
            first_char = current[0]
            last_char = current[-1]
            new_string = first_char + last_char
            current = new_string
        else: # lines with 1 character
            new_string = current[0] * 2
        lines[i] = new_string
    
    lines = [int(line) for line in lines]

    answer1 = sum(lines)
    print("Answer:", answer1)