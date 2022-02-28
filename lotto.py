# Write a Python script called lotto.py that will generate and display 6 unique random lottery numbers between 1 and 50.
# Think about which Python data structure is best suited to store the numbers.
# Use the Python help() function to find out which function to use from the python standard library called random.

import random

lotto_range = list(range(1,51))

num_set = set()

while len(num_set) != 6:
    num = random.choice(lotto_range)
    print(num)
    num_set.add(num)

print(num_set)