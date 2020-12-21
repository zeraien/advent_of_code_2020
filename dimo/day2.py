from collections import OrderedDict
from collections import Counter
from shared import load_file

def process_policy(policy):
	n_range, letter = policy.split(" ")
	n_range = [int(v) for v in n_range.split("-")]
	return n_range, letter

def validate2(policy, word):
	n_range, letter = process_policy(policy)
	def _try(x):
		try:
			return word[n_range[x]-1]==letter and 1 or 0
		except IndexError:
			return 0
	valid = _try(0)+_try(1) == 1
	#print(valid, word, policy)
	return valid

def validate1(policy, word):
	n_range, letter = process_policy(policy)
	counter = Counter(word)
	valid = letter in counter and counter[letter]>=n_range[0] and counter[letter]<=n_range[1]
	#print(valid, word, policy, counter)
	return valid

def run():
	# part 1
	count1 = 0
	for k,v in load_file("day2.json"):
		if validate1(k,v):
			count1+=1
	print("Part 1:",count1)

	# part 2
	count2 = 0
	for k,v in load_file("day2.json"):
		if validate2(k,v):
			count2+=1
	print('Part 2:', count2)

if __name__=="__main__":
	run()
