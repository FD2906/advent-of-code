with open('Day 1\input.txt') as file:
    file_contents = file.read()
    first_split = file_contents.split("\n\n")
    second_split = [element.split("\n") for element in first_split]
    totals_list = []
    for collection in second_split:
        current_total = 0
        for element in collection:
            if element != '':
                current_total += int(element)
        totals_list.append(current_total)
    print(max(totals_list)) # star 1
    sorted_list = sorted(totals_list)
    print(sum(sorted_list[-3:])) # star 2



    