# what is wrong with this?:
cheese = ['Cheddar', 'Stilton', 'Cornish Yarg']
cheese += 'Oke'
# It prints each character instead of Oke as an item itself

# how should 'oke' be added to the end of the cheese list?
cheese += ['Oke']
print(cheese)

# How would you add two new cheeses to the list with a single command?
cheese += ['Brie','Camembert']
print(cheese)