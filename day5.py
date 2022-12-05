from get_input import get_input
from collections import defaultdict


raw_input = get_input(day=5)


def main():

	main_data, moves = raw_input.split('\n\n')
	main_data = main_data.splitlines()

	moves = [i.split() for i in moves.splitlines()]
	moves = [[int(i) for i in move if i.isdigit()] for move in moves]

	idxs = [int(i) for i in main_data[-1].split()]
	main_data = main_data[:-1]


	main_dict = defaultdict(list)
	line_len = len(main_data[0])

	tuple_idx = zip(idxs, list(range(1, line_len, 4)))

	for idx1, idx2 in tuple_idx:
		main_dict[idx1] = [a[idx2] for a in main_data if a[idx2].isalpha()]
	
	return moves, main_dict


# Part 1 

moves, main_dict = main()

for line in moves:
	qty, orig, dest = line
	for _ in range(qty):
		to_move = main_dict[orig].pop(0)
		main_dict[dest].insert(0, to_move)

print(''.join([v[0] for k,v in main_dict.items()]))


# Part 2

moves, main_dict = main()

for line in moves:
	qty, orig, dest = line
	to_move = [main_dict[orig].pop(0) for _ in range(qty)]

	to_move.reverse()
	for char in to_move:
		main_dict[dest].insert(0, char)

print(''.join([v[0] for k,v in main_dict.items()]))

