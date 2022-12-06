from get_input import get_input


raw_input = get_input(day=6)


def main(str_input, marker_size):
	str_input_orig = str_input
	while str_input:
		look_at, str_input = str_input[:marker_size], str_input[1:]
		if len(set(look_at)) >= marker_size:
			break

	return str_input_orig.index(look_at) + marker_size


print(main(raw_input, marker_size=4))  # Part 1 
print(main(raw_input, marker_size=14)) # Part 2

