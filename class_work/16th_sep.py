# class Employee:
    
#     def __init__(self, fname, lname, salary, age, joining_date_str):
#         self.fname = fname
#         self.lname = lname
#         self.__salary = self.validate_salary(salary)
#         self._age = age
#         self.experience = Employee.calculate_years_of_service(joining_date_str)

#     @property
#     def age(self):
#         return self._age

#     @age.setter
#     def age(self, new_age):
#         self._age = new_age

#     def get_salary(self):
#         return self.__salary
    
#     def set_salary(self, salary):
#         self.__salary = self.validate_salary(salary)

#     def validate_salary(self, salary):
#         if (salary <= 0):
#             raise Exception("Salary must be greater than 0")
#         else:
#             return salary
        
#     @classmethod
#     def create_instance(self):
#         return Employee("test", "test", 100, 30)
    
#     @staticmethod
#     def calculate_years_of_service(joining_date_str):
#         from datetime import datetime
#         joining_date = datetime.strptime(joining_date_str, "%Y-%m-%d")
#         return (datetime.now() - joining_date).days


# emp1 = Employee("Muhammad", "Huzaifa", 1000, 20, "2023-08-01")
# print(emp1.fname, emp1.get_salary())

# emp1.set_salary(500)

# print(emp1.get_salary())

# print(emp1.age)


# emp1.age = 40

# print(emp1.age)

# print(emp1.experience)


# METHOD RESOLUTION ORDER

class Animal:

    def __init__(self, name, color):
        self.name = name
        self.color = color