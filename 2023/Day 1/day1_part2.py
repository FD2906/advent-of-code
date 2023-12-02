with open("input.txt") as data:
	lines = [] # populate the lines list with clean data

	file_contents = data.readlines()
	for line in file_contents:
		lines.append(line)

	lines = [line.strip("\n") for line in lines] # each list element contains separate line

	print(lines)

	print("\n_____________________________________\n")

	answer2 = 0 # tracking final answer

	# lines now contains only strings with alphanumerical characters
	# individually search for one, two, three ... or just digits

	for item in lines:
		if item != '':
			counter = ""
			for i in range(len(item)):
				if item[i] == 'o' and item[i+1] == 'n' and item[i+2] == 'e':
					counter += '1'
					break
				if item[i] == 't' and item[i+1] == 'w' and item[i+2] == 'o':
					counter += '2'
					break
				if item[i] == 't' and item[i+1] == 'h' and item[i+2] == 'r' and item [i+3] == 'e' and item [i+4] == 'e' :
					counter += '3'
					break
				if item[i] == 'f' and item[i+1] == 'o' and item[i+2] == 'u' and item[i+3] == "r":
					counter += '4'
					break
				if item[i] == 'f' and item[i+1] == 'i' and item[i+2] == 'v' and item [i+3] == 'e':
					counter += '5'
					break
				if item[i] == 's' and item[i+1] == 'i' and item[i+2] == 'x':
					counter += '6'
					break
				if item[i] == 's' and item[i+1] == 'e' and item[i+2] == 'v' and item [i+3] == 'e' and item [i+4] == 'n' :
					counter += '7'
					break
				if item[i] == 'e' and item[i+1] == 'i' and item[i+2] == 'g' and item [i+3] == 'h' and item [i+4] == 't' :
					counter += '8'
					break
				if item[i] == 'n' and item[i+1] == 'i' and item[i+2] == 'n' and item [i+3] == 'e' :
					counter += '9'
					break
				if item[i].isdigit():
					counter += item[i]
					break
			for j in range(len(item)): # a backwards search must be completed as well, to find the num at back
				k = -1-j
				if item[k] == 'o' and item[k+1] == 'n' and item[k+2] == 'e':
					counter += '1'
					break
				if item[k] == 't' and item[k+1] == 'w' and item[k+2] == 'o':
					counter += '2'
					break
				if item[k] == 't' and item[k+1] == 'h' and item[k+2] == 'r' and item [k+3] == 'e' and item [k+4] == 'e' :
					counter += '3'
					break
				if item[k] == 'f' and item[k+1] == 'o' and item[k+2] == 'u' and item[k+3] == "r":
					counter += '4'
					break
				if item[k] == 'f' and item[k+1] == 'i' and item[k+2] == 'v' and item [k+3] == 'e':
					counter += '5'
					break
				if item[k] == 's' and item[k+1] == 'i' and item[k+2] == 'x':
					counter += '6'
					break
				if item[k] == 's' and item[k+1] == 'e' and item[k+2] == 'v' and item [k+3] == 'e' and item [k+4] == 'n' :
					counter += '7'
					break
				if item[k] == 'e' and item[k+1] == 'i' and item[k+2] == 'g' and item [k+3] == 'h' and item [k+4] == 't' :
					counter += '8'
					break
				if item[k] == 'n' and item[k+1] == 'i' and item[k+2] == 'n' and item [k+3] == 'e' :
					counter += '9'
					break
				if item[k].isdigit():
					counter += item[k]
					break
			answer2	 += int(counter)
	
	print("Answer: {a}".format(a = answer2))