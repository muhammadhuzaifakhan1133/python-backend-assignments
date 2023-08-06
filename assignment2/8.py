# 8. Write a Python program to get the largest number from a list and use for loop consider the list [3, 5, 2, 1, 4]
# output should be 5

lst = [3, 5, 2, 1, 4]
largest = 0

for e in lst:
    if e > largest:
        largest = e

print(largest)