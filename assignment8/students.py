class Student:
    
    available_courses = ["English", "Urdu", "Physics", "Math", "Chemistry"]

    def __init__(self, name:str, age:int, courses:list):
        self.name = name
        self.age = age
        self.course = []
        self.enroll(courses)

    def display_info(self):
        print(f"{self.name} is {self.age} years old")

    def enroll(self, courses:list):
        for course in courses:
            if (course in Student.available_courses):
                self.course.append(course)
                print(f"{self.name} is now enrolled in {course}")
            else:
                print(f"Course {course} is not available")

    def list_courses(self):
        print(f"{self.name} is enrolled in following courses")
        print(", ".join(self.course))
    
    def list_available_courses(self):
        print(f"Available Courses are: ")
        print(", ".join(Student.available_courses))

std1 = Student("Huzaifa", 20, ["Physics"])
std1.display_info()
std1.enroll(["Urdu", "Computer Science", "Math"])
std1.list_courses()
std1.list_available_courses()