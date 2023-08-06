# 7. Write a Python program to sum all the items in a list use for loop. consider the list [3, 5, 2, 1, 4]
# output should be 15

lst = [3, 5, 2, 1, 4]
sum_result = 0

for i in lst:
    sum_result += i

print(sum_result)