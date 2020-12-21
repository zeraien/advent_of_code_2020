import json

def load_file(name):
	with open(name,'r') as f:
		data = json.load(f)
	return data
