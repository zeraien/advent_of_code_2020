from operator import and_

def load_file():
	groups = []
	people = []
	with open('day6.txt','r') as f:
		for line in f:
			if len(line)>1:
				people.append(line.strip())
			else:
				groups.append(people)
				people = []
		groups.append(people)
	return groups

def group_answer_count(group):
	return len(set(''.join(group)))

def group_answer_and(group):
	values = [set(a) for a in group]
	while len(values)>1:
		full_set = and_(*values[0:2])
		values = [full_set]+values[2:]
	answers = values[0]
	return len(answers)

groups = load_file()

print(sum([group_answer_count(group) for group in groups]))
print(sum([group_answer_and(group) for group in groups]))