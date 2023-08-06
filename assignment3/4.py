# 4. Write a Python program to print a specified list after removing the 0th, 4th and 5th elements using for loop. Sample List : ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow'] Expected Output : ['Green', 'White', 'Black']

lst = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']

lst.pop(0)
lst.pop(3) # after remove above 4th will be 3rd
lst.pop(3) # after remove above two values, 5th will be 3rd

print(lst)