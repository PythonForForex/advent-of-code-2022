#%%
from get_input import get_input


raw_input = get_input(day=1)

print(max([sum([int(b) for b in i.split()]) for i in raw_input.split('\n\n')]))


## Part 2


all_call = [sum([int(b) for b in i.split()]) for i in raw_input.split('\n\n')]
print(sum(sorted(all_call)[-3:]))

# %%
