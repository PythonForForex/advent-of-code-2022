from get_input import get_input


raw_input = get_input(day=2)


def calc_score():
	score = 0
	for i in raw_input.splitlines():
		q, w = i.split()
		op = opponent[q]
		score += op.get(w, 0)
		score += mine.get(w)

	return score


# Part 1 
mine = {'X': 1, 'Y': 2, 'Z': 3}
opponent = {
	'A': {'Y': 6, 'X': 3},
	'B': {'Z': 6, 'Y': 3},
	'C': {'X': 6, 'Z': 3}
}

print(calc_score())


## Part 2
mine = {'X': 0, 'Y': 3, 'Z': 6}
opponent = {
	'A': {'X': 3, 'Y': 1, 'Z': 2}, 
	'B': {'X': 1, 'Y': 2, 'Z': 3}, 
	'C': {'X': 2, 'Y': 3, 'Z': 1}, 
}

print(calc_score())
