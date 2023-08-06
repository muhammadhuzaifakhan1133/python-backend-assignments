# Write a program that accepts 3 inputs from user. input 1 and input 2 should be numbers and the third input should be mathematical operator. Perform operation accordingly

# for example
# input1 is 5 and input2 is 10 and input3 is +
# then output should be 15

# input1 is 5 and input2 is 10 and input3 is *
# then output should be 50

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
oper = input("Enter Operator (+, -, *, /): ")
result = None

if (oper == "+"):
    result = num1 + num2
elif (oper == "-"):
    result = num1 - num2
elif (oper == "*"):
    result = num1 * num2
elif (oper == "/"):
    result = num1 / num2
else:
    result = "Please correct right operator"

print(result)