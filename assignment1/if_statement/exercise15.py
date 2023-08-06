# Write a program to trace your subject mark. Your program should fulfill the following conditions:

# If the subject mark is below 0 and above 100, print “error: mark should be between 0 and 100 only”
# display "you are fail" if their mark is below 50.
# display "you are pass" if they score 50 and above.
# If subject mark is between 50 and 60, Remark: Good
# If subject mark is between 60 and 80, Remark: Very Good
# If subject mark is between 80 and 100, Remark: Outstanding

marks = int(input("Enter marks: "))

if (marks >= 0 and marks <= 100):
    if (marks >= 50):
        print("you are pass")
        if (marks >= 80):
            print("Remark: Outstanding")
        elif (marks >= 60):
            print("Remark: Very Good")
        else:
            print("Remark: Good")
    else:
        print("you are fail")
else:
    print("error: mark should be between 0 and 100 only")