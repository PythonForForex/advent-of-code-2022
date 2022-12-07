from get_input import get_input
from collections import defaultdict


raw_input = get_input(day=7)

dirs = defaultdict(int)
current_dir = None
for line in raw_input.splitlines():
	if '$' in line and 'cd' in line:
			next_dir = line.split()[2]
			if next_dir == '/':
				current_dir = next_dir
			elif next_dir == '..':
				current_dir = current_dir[:current_dir.rfind('/')]
			else:
				current_dir = f'{current_dir}/{next_dir}'
	
	first = line.split()[0]
	if first.isdigit():
		dirs[current_dir] += int(first)
		temp_dir = current_dir
		while temp_dir:
			temp_dir = temp_dir[:temp_dir.rfind('/')]
			dirs[temp_dir] += int(first)
			

# Part 1 

print(sum([i for i in dirs.values() if i < 100000]))


# Part 2 

total_space = 70000000
unused_needed = 30000000
free_space = total_space - dirs['/']
free_needed = unused_needed - free_space

print(sorted([i for i in dirs.values() if i > free_needed])[0])

