# Write a program that accepts 3 input from user and check the second is largest.

# for example:
# input1 is 5 and input2 is 10 and input3 is 15
# output should be 10 as this number is larger than 5 and smaller than 15

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))

if (num1 < num2 and num1 > num3) or (num1 < num3 and num1 > num2):
    print(f"{num1} is second largest")
elif (num2 < num1 and num2 > num3) or (num2 < num3 and num2 > num1):
    print(f"{num2} is second largest")
elif (num3 < num1 and num3 > num2) or (num3 < num2 and num3 > num1):
    print(f"{num3} is second largest")