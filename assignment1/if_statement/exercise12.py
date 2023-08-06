# Write a program that accepts 3 input from user and check which number is largest.

# for example:
# input1 is 5 and input2 is 10 and input3 is 15
# output should be 15 as this number is larger than 5 and 10

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

if (num1 > num2 and num1 > num3):
    print(f"{num1} is the largest")
elif (num2 > num1 and num2 > num3):
    print(f"{num2} is the largest")
elif (num3 > num1 and num3 > num2):
    print(f"{num3} is the largest")