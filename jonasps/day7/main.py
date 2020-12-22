bag_lines = []
lines = []
bags = []

with open('day7.txt') as file:
	for line in file:
		lines.append(line)
		if "shiny gold " in line and not line.startswith("shiny gold "):
			bag_lines.append(line)
			tokens = line.split(' ')
			bags.append('{0} {1} '.format(tokens[0], tokens[1]))

for bag in bags:
	for line in lines:
		if not line.startswith(bag):
			if bag in line:
				bag_lines.append(line)
				tokens = line.split(' ')
				bags.append('{0} {1} '.format(tokens[0], tokens[1]))			
				bag_lines.append(line)
for bag in bags:
        for line in lines:
                if not line.startswith(bag):
                        if bag in line:
                                bag_lines.append(line)
                                tokens = line.split(' ')
                                bags.append('{0} {1} '.format(tokens[0], tokens[1]))
                                bag_lines.append(line)


set_bags = set(bag_lines)
print(len(set_bags))
			
