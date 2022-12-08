from get_input import get_input
import numpy as np


raw_input = get_input(day=8)
raw_input = [[*map(int, b)] for b in raw_input.splitlines()]
raw_input = np.matrix(raw_input)
max_range = len(raw_input)

# Part 1 

visibile = max_range * 4 -4
for y in range(1, max_range-1):
	for x in range(1, max_range-1):

		num = raw_input[x,y]

		check_left = [i<num for i in raw_input[x, :y]]
		check_right = [i<num for i in raw_input[x, y+1:]]
		check_up = [i<num for i in raw_input[:x, y]]
		check_down = [i<num for i in raw_input[x+1:, y]]

		if np.any([np.all(check_left), np.all(check_right), np.all(check_up), np.all(check_down)]):
			visibile +=1


print(f'Part 1 - {visibile}')


# Part 2

best = 0

def get_val(a, x=None, y=None):
	if x is not None:
		return raw_input[x, a]
	if y is not None:
		return raw_input[a, y]


def main(list_to_iter, num, x=None, y=None):
	grand = 1
	for item in list_to_iter:
		total = 0
		for a in item:
			val = get_val(a, x, y)	
			total +=1
			if val >= num:
				break

		if total: 
			grand *= total
	
	return grand


for x in range(max_range):
	for y in range(max_range):
		num = raw_input[x,y]
		all_x = [range(y-1, -1, -1), range(y+1, max_range)]
		all_y = [range(x-1, -1, -1), range(x+1, max_range)]
		xx = main(all_x, num, x, None)
		yy = main(all_y, num, None, y)
		best = max(best, xx*yy)


print(f'Part 2 - {best}')	

