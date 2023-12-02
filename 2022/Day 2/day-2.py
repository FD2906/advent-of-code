# A = rock, B = paper, C = scissors
# X = rock, Y = paper, Z = scissors
# winner = highest score
# win = 6 points, draw = 3 points, loss = 0 points
# rock = 1 point, paper = 2 points, scissors = 3 points
# combos: 
# A Z / B X / C Y = 6 points
# A X / B Y / C Z = 3 points
# A Y / B z / C X = 0 points


with open("Day 2\input.txt") as file:
    contents = file.readlines()
    new_contents = [element.strip("\n") for element in contents]
    print(new_contents)

    win_val = 6
    draw_val = 3

    scissors_val = 3
    paper_val = 2
    rock_val = 1

    total = 0

    for element in new_contents: 
        if element[-1] == "Z": # wins only
            total += win_val
            # individual checks on hand shape
            if element[0] == "A": # opp chose rock
                total += paper_val
            elif element[0] == "B": # opp chose paper
                total += scissors_val
            elif element[0] == "C": # opp chose scissors
                total += rock_val
        elif element[-1] == "Y": # draws only
            total += draw_val
            if element[0] == "A": 
                total += rock_val
            elif element[0] == "B":
                total += paper_val
            elif element[0] == "C":
                total += scissors_val
        elif element[-1] == "X": # losses only
            if element[0] == "A": 
                total += scissors_val
            elif element[0] == "B":
                total += rock_val
            elif element[0] == "C":
                total += paper_val
    

    print(total)

