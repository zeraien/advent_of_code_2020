import math

def load_file():
	with open("day5.txt", 'r') as f:
		lines = [line.strip() for line in f]
	return lines

def algo(line, pos, range_, split_down, split_up):
	length = len(range_)
	half = int(round(length/2))
	if pos>=len(line):
		return range_

	if line[pos] == split_down:
		new_range = range_[:half]
	elif line[pos] == split_up:
		new_range = range_[half:]
	else:
		return range_
	
	return algo(line, pos=pos+1, range_=new_range, split_down=split_down, split_up=split_up)

def get_row(line):
	return algo(line, pos=0, range_=range(128), split_down='F', split_up='B')[0]

def get_col(line):
	return algo(line[7:], pos=0, range_=range(8), split_down='L', split_up='R')[0]

def get_seat(line):
	row = get_row(line)
	col = get_col(line)
	seat = row*8+col
	return seat

def find_empty_seat(seats):
	for idx,seat in enumerate(seats):
		if idx==0 or idx==len(seats)-1:
			continue
		seat = seats[idx]
		next_seat = seats[idx+1]
		if next_seat-seat==2:
			return next_seat-1
	return None

def run():
	lines = load_file()
	seats = sorted([get_seat(line) for line in lines])
	print('part 1: %s'% max(seats))
	print('part 2: %s' % find_empty_seat(seats))

if __name__=="__main__":
	run()