import re
from collections import defaultdict

mybag = "shiny gold"

def load_file():
	bags = defaultdict(set)
	bags_with_counts = defaultdict(dict)
	with open('day7.txt', 'r') as f:
		for line in f:
			match = re.fullmatch(r"([\w\s]+) bags? contain (.*).",line.strip())
			if match:
				outer_bag, inner_bags = match.groups()
				inner_matches = [re.fullmatch(r"(\d+) ([\w\s]+) bags?", p.strip()) for p in inner_bags.split(', ')]
				for inner_match in inner_matches:
					if inner_match:
						count, inner_bag = inner_match.groups()
						bags[inner_bag].add(outer_bag)
						bags_with_counts[outer_bag][inner_bag] = int(count)

	return bags, bags_with_counts


def count_containers(active_bag, bags):
	collection = set()
	if active_bag in bags:
		for outer_bag in bags[active_bag]:
			collection.add(outer_bag)
			collection |= count_containers(outer_bag, bags=bags)
	return collection
def _recursive_bag_counter(active_bag, bags):
	count = 0
	if active_bag in bags:
		for inner_bag, inner_count in bags[active_bag].items():
			count += inner_count
			count += inner_count * _recursive_bag_counter(inner_bag,
			 	bags=bags)
	return count

def run():
	bags, bags_with_counts = load_file()
	color_count = len(count_containers(mybag, bags))

	print('part 1', color_count)
	print('part 2', _recursive_bag_counter(mybag, bags_with_counts))

if __name__=="__main__":
	run()