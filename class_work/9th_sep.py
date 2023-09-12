# count = 0

# def increment():
#     global count
#     count += 1

# def decrement():
#     global count
#     count -= 1

# increment()
# increment()
# increment()
# increment()
# increment()
# decrement()
# decrement()
# print(count)

class Employee:
    count = 0
    def __init__(self, fname, lname, salary):
        self.fname = fname
        self.lname = lname
        self.salary = salary
        Employee.count += 1

    def get_fullname(self):
        return self.fname + " " + self.lname
    
    def get_email(self):
        return self.fname + self.lname + "@gmail.com"

emp1 = Employee("Muhammad", "Huzaifa", 5000)
print(emp1.get_email())
print(Employee.count)

emp2 = Employee("Muhammad", "Anas", 10000)
print(emp2.get_email())
print(Employee.count)