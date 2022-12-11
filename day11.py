from get_input import get_input


def parse_input():
	raw_input = get_input(day=11)
	raw_input = raw_input.split('\n\n')
	monkeys = {}
	clean_up = {
		'divisible by ': '',
		'throw to monkey ': '', 
		'If true': 'True',
		'If false': 'False'
	}
	for lines in raw_input:
		line = lines.splitlines()
		idx = line.pop(0)
		idx = int(''.join([i for i in idx if i.isdigit()]))
		monkeys[idx] = {'inspected': 0}
		for l in line: 
			k, v = l.split(':')
			for x,y in clean_up.items():
				v = v.strip().replace(x, y)
				k = k.strip().replace(x, y)

			if 'Starting items' in k:
				v = [int(a) for a in v.split(',')]
			elif 'Operation' in k:
				v = v[v.find('=')+2:]
			elif v.isdigit():
				v = int(v)

			monkeys[idx][k] = v

	lcm = 1
	t = [i['Test'] for i in monkeys.values()]
	for num in t:
		lcm *= num

	return monkeys, lcm


def main(rounds):
	monkeys, lcm = parse_input()
	for _ in range(rounds):
		for monkey in monkeys.values():
			while monkey['Starting items']:
				old = monkey['Starting items'].pop(0)
				monkey['inspected'] += 1
				new = eval(monkey['Operation'])
				new = new % lcm if rounds == 10_000 else new // 3

				next_monkey = new % monkey['Test'] == 0
				next_monkey = monkey[str(next_monkey)]
				monkeys[next_monkey]['Starting items'].append(new)
	
	monkey_business = sorted([v['inspected'] for v in monkeys.values()])[-2:]
	return monkey_business[0] * monkey_business[1]


print(f'Part 1: {main(20)}')
print(f'Part 2: {main(10_000)}')

