def print_adjacent(matrix, row_index, column_index):
    north = east = south = west = None
    northeast = southeast = southwest = northwest = None
    """
    north = i - 1, j
    south = i + 1, j
    east = i, j + 1
    west = i, j - 1
    northeast = i - 1, j + 1
    southeast = i + 1, j + 1
    southwest = i + 1, j - 1
    northwest = i - 1, j - 1
    """

    # if i, j = 0, then top left corner, so only east, south, and southeast possible 
    try:
        north = matrix[row_index - 1][column_index]
        south = matrix[row_index + 1][column_index]
        east = matrix[row_index][column_index + 1]
        west = matrix[row_index][column_index - 1]
        northeast = matrix[row_index - 1][column_index + 1]
        southeast = matrix[row_index + 1][column_index + 1]
        southwest = matrix[row_index + 1][column_index - 1]
        northwest = matrix[row_index - 1][column_index - 1]
    except IndexError or (row_index == -1) or (column_index == -1):
        pass

    print("""
North = {}
South = {}
East = {}
West = {}
NorthEast = {}
SouthEast = {}
SouthWest = {}
NorthWest = {}
""".format(north, south, east, west, northeast, southeast, southwest, northwest))
    




with open("2023\Day 3\input.txt") as file:
    data = [line.strip("\n") for line in file.readlines()]
    #print(data) 

    matrix = []
    # form a matrix, split every character up in each line
    for line in data:
        new_row = []
        for char in line:
            new_row.append(char)
        matrix.append(new_row)
    
    print(matrix)
    print("Dimensions: {a} across, {b} down".format(a = len(matrix[0]), b = len(matrix)))

    for i in range(len(matrix)): # i is the index of matrix
        current_row = matrix[i]
        for j in range(len(current_row)): # j is the index of the current_row
            current_char = matrix[i][j]

    print_adjacent(matrix, 0, 0)