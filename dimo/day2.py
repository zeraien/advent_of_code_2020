import re
from collections import OrderedDict
from collections import Counter
from dataclasses import dataclass

@dataclass
class Line:
	lower:int
	upper:int
	char:str
	passwd:str

def process_line(line):
	match = re.match(r"^(\d+)-(\d+) ([a-z]): ([a-z]+)$", line)
	if match:
		groups = match.groups()
		return Line(lower=int(groups[0]), upper=int(groups[1]), char=groups[2], passwd=groups[3])
	raise ArgumentError("Invalid line: %s"%line)

def load_file():
	lines = []
	with open("day2.txt","r") as f:
		lines = [process_line(line) for line in f]
	return lines

def validate2(line):
	n_range = [line.lower,line.upper]
	def _try(x):
		return line.passwd[n_range[x]-1]==line.char and 1 or 0
	valid = _try(0)+_try(1) == 1
	#print(valid, word, policy)
	return valid

def validate1(line):
	n_range = [line.lower,line.upper]
	counter = Counter(line.passwd)
	valid = line.char in counter and n_range[0]<=counter[line.char]<=n_range[1]
	#print(valid, word, policy, counter)
	return valid

def run():
	# part 1
	count1 = 0
	lines = load_file()
	for line in lines:
		if validate1(line):
			count1+=1
	print("Part 1:",count1)

	# part 2
	count2 = 0
	for line in lines:
		if validate2(line):
			count2+=1
	print('Part 2:', count2)

if __name__=="__main__":
	run()
