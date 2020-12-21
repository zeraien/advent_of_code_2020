import re
from collections import Counter

def val_year(_min, _max):
	def v(x):
		if x and re.match(r"^\d{4}$",x):
			return _min <= int(x) <= _max
		return False
	return v
def val_height(x):
	if x:
		m = re.match(r"^(\d+)(cm|in)$",x)
		if m:
			v, u = m.groups()
			v = int(v)
			if u=='cm':
				return 150<=v<=193
			elif u=='in':
				return 59<=v<=76

	return False

def val_ecl(x):
	VALID = "amb blu brn gry grn hzl oth".split(' ')
	return x in VALID

def val_pid(x):
	return x and (re.match(r"^\d{9}$",x) is not None)

def val_hcl(x):
	return x and (re.match(r"^#[0-9a-f]{6}$", x) is not None)

REQUIRED_FIELDS={
	'byr':val_year(1920,2002),
	'iyr':val_year(2010, 2020),
	'eyr':val_year(2020,2030),
	'hgt':val_height,
	'hcl':val_hcl,
	'ecl':val_ecl,
	'pid':val_pid,
}

def load_file(name="day4.txt"):
	passports = []
	active_passport = {}

	with open(name,'r') as f:
		lines = f.readlines()
	for line in lines:
		if len(line)>1:
			items = line.strip().split(" ")
			for item in items:
				key, value = item.split(":")
				active_passport[key] = value
		else:
			passports.append(active_passport)
			active_passport = {}

	# gotta add the last password to the list!
	passports.append(active_passport)

	return passports

def has_all_fields(passport):
	return Counter([passport.get(k) for k in REQUIRED_FIELDS.keys()])[None] == 0

def is_valid(passport):
	if has_all_fields(passport):
		has_error = False
		for key, valfunc in REQUIRED_FIELDS.items():
			valid = valfunc(passport[key])
			if not valid:
				has_error = True
				break

		return not has_error
	return False

def count_valid1(passports):
	counter = 0
	for passport in passports:
		if has_all_fields(passport):
			counter+=1
	return counter

def count_valid2(passports):
	counter = 0
	for passport in passports:
		if is_valid(passport):
			counter+=1
	return counter

print("Valid passports part 1: %s" % count_valid1(load_file()))
print("Valid passports part 2: %s" % count_valid2(load_file()))