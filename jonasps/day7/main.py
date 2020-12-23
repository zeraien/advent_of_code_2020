
#part 1
# bag_lines = []
# lines = []
# bags = []
# with open('day7.txt') as file:
# 	for line in file:
# 		lines.append(line)
# 		if "shiny gold " in line and not line.startswith("shiny gold "):
# 			bag_lines.append(line)
# 			tokens = line.split(' ')
# 			bags.append('{0} {1} '.format(tokens[0], tokens[1]))

# for bag in bags:
# 	for line in lines:
# 		if not line.startswith(bag):
# 			if bag in line:
# 				bag_lines.append(line)
# 				tokens = line.split(' ')
# 				bags.append('{0} {1} '.format(tokens[0], tokens[1]))			
# 				bag_lines.append(line)
# for bag in bags:
#         for line in lines:
#                 if not line.startswith(bag):
#                         if bag in line:
#                                 bag_lines.append(line)
#                                 tokens = line.split(' ')
#                                 bags.append('{0} {1} '.format(tokens[0], tokens[1]))
#                                 bag_lines.append(line)

# set_bags = set(bag_lines)
# print(len(set_bags))

#part 2
b_tree = {}

def parse_bag(bag_line, bag_tree):
	tokens = [ x for x in bag_line.strip().split(' ') if x not in ['bag', 'bags']]
	bag = '{0} {1}'.format(tokens[0], tokens[1])
	tokens = tokens[tokens.index('contain')+1:]
	end = len(tokens) -1
	contain_bags = []
	for i in range(0, end, 3):
		if i+2 <= end:
			contain_bags.append(('{0} {1}'.format(tokens[i+1], tokens[i+2]), tokens[i]))
	bag_tree[bag] = contain_bags

with open('day7.txt') as file:
	for line in file:
		parse_bag(line.replace(',','').replace('.',''), b_tree)

def calc_num_of_bags(bag_name, tree, multip, total):
	in_this_bag = sum([int(x[1]) for x in tree[bag_name]])
	_total = total
	in_this = 0
	for y in tree[bag_name]:
		in_this += calc_num_of_bags(y[0], tree, int(y[1]), _total)
	return _total + (in_this + in_this_bag) * multip
		

current_bag = 'shiny gold'
result = calc_num_of_bags(current_bag, b_tree, 1, 0)

print(result)
