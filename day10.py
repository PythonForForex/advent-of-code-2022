from get_input import get_input

raw_input = get_input(day=10)
raw_input= raw_input.splitlines()

x= 1 
fut_actions = {}
result = 0
crt = []

for idx in range(240):
	crt_pos = idx
	while crt_pos >= 40:
		crt_pos -= 40

	line = raw_input[idx] if idx < len(raw_input) else 'noop'
	pos = max(fut_actions.keys()) if fut_actions else idx

	if 'addx' in line:
		action, qty = line.split()
		fut_actions[pos+2] = int(qty)
	else:
		fut_actions[pos+1] = 0
	
	if fut_actions:
		for k,v in fut_actions.copy().items():
			if k ==idx:
				x += v
				del fut_actions[k]

	if idx+1 in [20, 60, 100, 140, 180, 220]:
		result += ((idx+1) * x)

	sprite = [x-1, x, x+1]
	if crt_pos in sprite:
		crt.append('#')
	else:
		crt.append('.')


print('Part 1: ', result)

print('Part 2: ')
for _ in range(7):
	popped = crt[:40]
	del crt[:40]
	print(''.join(popped))

