from get_input import get_input


raw_input = get_input(day=3)
raw_input = raw_input.splitlines()


def num_value(common_list):
	points = 0
	for val in common_list:
		adj = 96 if val.islower() else 38
		points += ord(val) - adj
	
	return points


# Part 1 

total_score = 0
for line in raw_input:
	idx = len(line) // 2
	first = line[idx:]
	second = line[:idx]
	common = set([i for i in list(first) if i in list(second)])
	total_score += num_value(common)

print(total_score)


# Part 2

total_sum = 0
while raw_input:
	first, second, third, *raw_input = raw_input
	common = [i for i in first if i in second and i in third]
	total_sum += num_value(set(common))

print(total_sum)

