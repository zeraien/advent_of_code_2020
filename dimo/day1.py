import random
import math
from shared import load_file


numbers = load_file("day1.json")

def calc(*n):
	v = 2020
	if sum(*n)==v:
		return n, math.prod(*n)
	return False

def get_n(n=2):
	return [random.choice(numbers) for foo in range(n)]

def run():
	length = len(numbers)
	
	#part 1
	end = False
	while not end:
		result = calc(get_n(2))
		if result != False:
			print("part 1", result)
			end=True
	
	# part 2
	end = False
	while not end:
		result = calc(get_n(3))
		if result != False:
			print("part 2", result)
			end=True
	
if __name__=="__main__":
	run()
