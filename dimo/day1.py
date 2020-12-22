import random
import math

def load_file():
	values = set()
	with open('day1.txt','r') as f:
		values = {int(line.strip()) for line in f}
	return list(values)

def calc(*n):
	v = 2020
	if sum(*n)==v:
		return n, math.prod(*n)
	return False

def perform(numbers, n=2):
	end = False
	while not end:
		result = calc(get_n(numbers, n=n))
		if result != False:
			print(result)
			end=True

def get_n(numbers, n=2):
	return [random.choice(numbers) for foo in range(n)]

def run():
	numbers = load_file()
	perform(numbers, 2)
	perform(numbers, 3)
	
if __name__=="__main__":
	run()
