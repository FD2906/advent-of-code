with open("2023\Day 4\input.txt") as file:
    answer1 = 0
    answer2 = 0
    
    contents = [line.strip("\n") for line in file.readlines()]
    #print(contents)
    cards_and_numbers = {}

    contents = [line.split(": ") for line in contents] # contents is a list
    for card in contents:
        # get card_number
        card_number = (card[0].split())[1] # 1, 2, 3 ... 210, 211, 212
        
        numbers = card[1].split(" | ") # list containing string of wins, string of scratches
        # get winning_numbers
        winning_numbers = (numbers[0]).split()
        # get scratch_numbers
        scratch_numbers = (numbers[1]).split()

        all_numbers = []
        all_numbers.append(winning_numbers)
        all_numbers.append(scratch_numbers)

        cards_and_numbers[int(card_number)] = all_numbers

    #print(cards_and_numbers) # {card_no : [ [winning nos], [scratch nos] ]}

    num_scratchcards = dict(zip(range(1, 213), [1 for i in range(212)])) # {1: 1, 2: 1, 3: 1, ... 212: 1}

    for card, all_numbers in cards_and_numbers.items():
        winning_numbers = all_numbers[0] 
        scratch_numbers = all_numbers[1]

        matches = len(set(winning_numbers) & set(scratch_numbers)) 
        print("Card {a} has {b} matches.".format(a = card, b = matches))

        cards_to_add = num_scratchcards[card] # starts at 1 but increases, etc

        for i in range(1, matches + 1): # i counts from 1, 2, 3, ... 10 for card 1
            card_to_change = card + i
            value_to_change = num_scratchcards[card_to_change]
            num_scratchcards[card_to_change] = value_to_change + cards_to_add
    

    print(num_scratchcards)
    answer2 = sum(num_scratchcards.values())
    print(answer2)


    

        
    



    