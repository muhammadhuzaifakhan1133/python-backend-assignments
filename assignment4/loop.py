# Write a Python program to copy a list using for loop. consider a list
# use for loop and add al the items in li_2

li = [1, 2, 3, 4]
li_2 = []

for e in li:
    li_2.append(e)

print(li_2)

# Write a Python function that takes two lists and returns True if they have at least one common member.
# consider list l1 = [1, 2, 3, 4] and l2 = [5, 6, 7, 3]
# in both list value "3" is common
# use for loop
# hint: nested loop

def common(l1, l2):
    for i in l1:
        for j in l2:
            if i == j:
                return True
    return False

a = [1, 2, 3, 4]
b = [5, 6, 7, 8]
print(common(a, b))

# Write a program to display index and the values (both) of a list using for loop. consider a list l = [100, 200, 300, 400]
# output: 
# 0 100
# 1 200
# 2 300
# 3 400

li = [100, 200, 300, 400]
for i, e in enumerate(li):
    print(i, e)

# Write a program that find common values between 2 lists and also tells how many times the common value occurs.
# consider the list l1 = ['a', 'b', 'c', 'd'] and l2 = ['e', 'b', 'g', 'd', 'f', 'h']
# output:
# {"a": 1, "b": 2, "c": 1, "d": 2, "e": 1, "f": 1, "g": 1, "h": 1}
# hint: use nested loop

def chars(l1, l2):
    chars = {}
    for i in l1:
        for j in l2:
            if i== j and i not in chars:
                chars[i] = min(l1.count(j), l2.count(j))
    return chars

a = ['a', 'b', 'c', 'd', 'b']
b = ['e', 'b', 'g', 'd', 'f', 'h', 'b', 'b']
print(chars(a, b))

# consider the number 2783, the number consists of 4 digits.
# Count the total number of digits in a number using while loop.
# instruction (hint):
# x = 2783
# counter = 0
# run while loop as long as x becomes 0
# increment the counter inside while loop
# divide x by 10 using floor division syntax "//"

def num_length(number):
    c = 0
    while number != 0:
        c += 1
        number = number // 10
    return c

print(num_length(3234))

# Write a program that takes user input and display it. The program keep ask user the input until user enters “0”

def zero_input():
    num = input("Enter a zero: ")
    while num != "0":
        num = input("Please enter zero: ")

zero_input()

# Write a program and ask user to enter number, 5 times using while loop. store each value in list.
# calculate the sum of all values in a list

def sum_of_input_list():
    c = 0
    li = []
    while c < 5:
        li.append(int(input("Enter a number: ")))
        c += 1
    s = 0
    for i in li:
        s += i
    return s

print(sum_of_input_list())

# Write a program to keep asking for a number until you enter a negative number. At the end, print the sum of all entered numbers.

def sum_of_nums():
    s = 0
    num = int(input("Enter a number: "))
    while num >= 0:
        s += num
        num = int(input("Enter a number: "))
    return s

print(sum_of_nums())

# Write a program to ask for a name until the user enters END. Print the name each time. When you are done, print "I am done."

def get_name():
    name = input("Enter name: ")
    while name != "END":
        print(name)
        name = input("Enter name: ")
    print("I am done")

get_name()

# consider the list l1 [11, 33, 50]. use for loop to output the result like "113350"

def join_string():
    l1 = [11, 33, 50]
    string = ""
    for e in l1:
        string += str(e)
    return string

print(join_string())


# Write a Python program to copy a dict using for loop. consider a dict
# use for loop and add al the items in d2

def copy_dict(d1):
    d2 = {}
    for k in d1:
        d2[k] = d1.get(k)
    return d2

d1 = {"id": 1, "name": "huzaifa", "gender": "male"}
print(copy_dict(d1))