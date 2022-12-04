from get_input import get_input


raw_input = get_input(day=4)


# Part 1 

count = 0

for i in raw_input.splitlines():
	nums = [b.split('-') for b in i.split(',')]
	nums = [int(item) for sublist in nums for item in sublist]

	first_low, first_high, second_low, second_high = nums

	if (first_low <= second_low and first_high >= second_high) or (first_low >= second_low and first_high <= second_high):
		count += 1

print(count)


# Part 2

count = 0

for i in raw_input.splitlines():
	nums = [b.split('-') for b in i.split(',')]
	nums = [int(item) for sublist in nums for item in sublist]

	if [i for i in range(nums[0], nums[1]+1) if i in range(nums[2], nums[3]+1)]:
		count+=1

print(count)

