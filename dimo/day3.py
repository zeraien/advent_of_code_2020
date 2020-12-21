import math

def load_file(name="day3.txt"):
	map_list = []
	with open(name,'r') as f:
		map_list = f.readlines()
	return [l.strip() for l in map_list]

def traverse(map_list, x_step=0, y_step=1):
	counter, x=0,0
	wrap_point = len(map_list[0])
	for idx in range(0, len(map_list), y_step):
		line = map_list[idx]
		if line[x]=="#":
			counter+=1
		x+=x_step
		x = x%wrap_point
	return counter

def traverse_alt(map_list):

	paths = [
		[1,1],
		[3,1],
		[5,1],
		[7,1],
		[1,2]
	]
	values = []
	for x,y in paths:
		values.append(traverse(map_list, x_step=x,y_step=y))
	return values, math.prod(values)

def run():
	print("Part 1: Hit %s trees" % traverse(load_file()))
	print("Part 2: Hit %s trees (product %s)" % traverse_alt(load_file()))
if __name__=="__main__":
	run()
