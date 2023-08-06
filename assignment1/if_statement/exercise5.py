# Write a program to display the grade of the user in subject A, ask user marks obtained out of 100

marks = int(input("Enter marks in IT: "))
per = (marks / 100) * 100
if per > 90:
    print("A+")
elif per > 80:
    print("A")
elif per > 70:
    print("B")
elif per > 60:
    print("C")
elif per > 50:
    print("D")
else:
    print("No Grade")