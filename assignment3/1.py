# 1. Write a Python program to multiply all the items in a list and use for loop. consider the list [3, 5, 2, 1, 4].
# output should be 360

product = 1
lst = [3, 5, 2, 1, 4]

for e in lst:
    product *= e

print(product)