with open("Day 2\input.txt") as data:
    contents = data.readlines()

    # strip \n
    contents = [line.strip("\n") for line in contents]
    # split each string at ;
    games = {} # dictionary with pair (id:games played)

    for index in range(len(contents)): # index will go from 0 to 99, remember to add 1
        game_id = index + 1 # integer for faster handling
        current_game = contents[index]
        current_game = current_game.split(": ")[1] # points towards cubes info
        current_game = current_game.split("; ") # current_game becomes a list of cubes
        games[game_id] = current_game # populates games dict


    # we need to rebuild each value for games so it has the form:
    # {1: [ ["4 red", "18 green", "15 blue"], ["17 green, 18 blue", "9 red"], ["8 red", "14 green", "6 blue"] ["14 green", "12 blue", "2 red"] ]}

    # go thru each value in dict
    for game_id, cubes_list in games.items():
        reconstructed_cubes_list = []
        #print(dict_key, cubes_list)
        for subset in cubes_list:
            lst_to_add = [] 
            # work on subset, first by splitting at ', ' and add each part to a lst_to_add, then append the entire lst_to_add to reconstructed_cubes_list
            subset_list = subset.split(", ")
            reconstructed_cubes_list.append(subset_list)
        games[game_id] = reconstructed_cubes_list
    
    print(games) # structure OK
    print("\n___________________________________\n")

    # will make it easy to sum up ids, 1 to 100

    possible_games = dict(zip(range(1, 101), [False for i in range(100)])) # master dict, filled up with {1: False, 2: False}, will be changed and used later

    # work by game.
    # check if red: split by space and get numbers by accessing sublist at [0], and making a new dict {red: 0, blue: 0, green: 0}
    # do same for if green, if blue
    # at end, check against red 12, green 13, blue 14

    # remember structure of games dict is # {1: [ ["4 red", "18 green", "15 blue"], ["17 green, 18 blue", "9 red"], ["8 red", "14 green", "6 blue"], ["14 green", "12 blue", "2 red"] ]}
    
    for game_id, cubes_list in games.items():
        # game_id will contain 1, 2, 3, ... , 99, 100.
        # cubes_list will contain [ ["4 red", "18 green", "15 blue"], ["17 green, 18 blue", "9 red"], ... ] at start

        game_id_pass = True # default state, becomes value in possible_games
        false_check_list = [True for i in range(len(cubes_list))] # [True, True, True, True] for id 1

        # if there are no falses in false_check_list, set game_id_pass to True 
        
        for i in range(len(cubes_list)): # subset = ["4 red", "18 green", "15 blue"], should contain index
            for cubes in cubes_list[i]: # cubes = "4 red" or "18 green" or "15 blue"
                total_reds = total_greens = total_blues = 0

                quantity = int(cubes.split()[0]) # gets 4 or 18 or 15
                if "red" in cubes:
                    total_reds += quantity
                elif "green" in cubes:
                    total_greens += quantity
                else:
                    total_blues += quantity

                if (total_reds > 12) or (total_greens > 13) or (total_blues > 14):
                    false_check_list[i] = False
        
        if False in false_check_list:
            game_id_pass = False # this means that there is a False in the list, so the overall game is not possible

        possible_games[game_id] = game_id_pass
    
    #print(possible_games)

    answer1 = 0

    for game_id, game_passed in possible_games.items():
        if game_passed:
            answer1 += game_id
    
    print("Answer 1:", answer1)
    print("\n___________________________________\n")

    # set up a new dict, min_games, with pairs game_id: power
    min_games = dict(zip(range(1, 101), [0 for i in range(100)]))

    # go thru each dict value, cubes_list
    for game_id, cubes_list in games.items():
        # set up a variable representing max_red, max_green, and max_blue, set all to 0
        min_red = min_green = min_blue = 0
        # go thru each subset
        for subsets in cubes_list: # subset = ["4 red", "18 green", "15 blue"]
            for cubes in subsets: # cubes = "4 red" or "18 green" or "15 blue"
                quantity = int(cubes.split()[0]) # find quantity using line: quantity = int(cubes.split()[0]) 
                if ("red" in cubes) and (quantity > min_red):
                    min_red = quantity
                elif ("green" in cubes) and (quantity > min_green):
                    min_green = quantity
                elif ("blue" in cubes) and (quantity > min_blue):
                    min_blue = quantity
        print("Game: {}. Minimum reds: {}, minimum greens: {}, minimum blues: {}".format(game_id, min_red, min_green, min_blue))
        current_power = min_red * min_green * min_blue
        min_games[game_id] = current_power

    # find sum of min_games.values() 
    print(min_games.values())
    answer2 = sum(min_games.values())
    print("Answer 2:", answer2)