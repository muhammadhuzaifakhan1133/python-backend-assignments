# Write a program that accepts 1 input from user and check if the number is divisible by 2 and 3 both.

# for example
# input1 is 10
# output should be "10 is only divisible by 2"

# input1 is 9
# output should be "9 is only divisible by 3"

# input1 is 12
# output should be "12 is divisible by 2 and 3"

num = int(input("Enter a number: "))
if num % 2 == 0 and num % 3 == 0:
    print("yes, It is divisible by 2 and 3 both")
else:
    print("no, It is not divisible by 2 and 3 both")