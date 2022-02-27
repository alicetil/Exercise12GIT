# Write a Python script called lotto.py that will generate and display 6 unique random lottery numbers between 1 and 50.
# Think about which Python data structure is best suited to store the numbers.
# Use the Python help() function to find out which function to use from the python standard library called random.

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
