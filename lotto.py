import random

lotto_range = list(range(1,51))
# print(lotto_range)

draws = 0
num_list = []

while draws < 6:
    num = random.choice(lotto_range)
    print(num)
    num_list += [num]
    draws = draws + 1

print(num_list)
