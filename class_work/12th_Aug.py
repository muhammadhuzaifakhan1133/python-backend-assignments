# l = [100, 200, 300, 400]
# for index, value in enumerate(l):
#     print(index, value)

l2 = [
    {
        "id": 1,
        "name": "Huzaifa",
        "is_employeed": True,
        "is_married": False,
    },
    {
        "id": 2,
        "name": "Ali",
        "is_employeed": True,
        "is_married": False,
    }
]

# for obj in l2:
#     if obj.get("name") == "Huzaifa":
#         print(obj)


# number = input("Enter a number between 1 to 10: ")
# while not(number.isdecimal()) or int(number) < 1 or int(number) > 10:
#     number = input("Please enter a valid number between 1 to 10: ")

# print("Valid Number is :", number)


# i = 1
# while i<=20:
#     print(i)
#     i += 1

# l1 = ["a", "b", "c", "d"]
# while len(l1) > 0:
#     print(l1)
#     l1.pop()
# print(l1)

def get_employee_by_id(id, employees):
    for emp in employees:
        if emp.get("id") == id:
            return emp
        
obj = get_employee_by_id(1, l2)
print(obj)

