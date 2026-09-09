class Student:
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        self.courses = []

    def enroll(self, course):
        self.courses.append(course)
        


class Teacher:
    def __init__(self, name, subject):
        self.name = name
        self.subject = subject
        self.students = []   

    def add_student(self, student):
        self.students.append(student)


student1 = Student("Ana", 9)
student2 = Student("Ben", 9)
student3 = Student("Carla", 9)
teacher1 = Teacher("Ms. Cruz", "Mathematics")
teacher1.add_student(student1)
teacher1.add_student(student2)
teacher1.add_student(student3)
for student in teacher1.students:
    print(student.name)

class Course:
    def __init__(self,name):
        self.name = name
        self.students = []  

math = Course("Mathematics")
science = Course("Science")

student1.enroll(math)
student1.enroll(science)
student2.enroll(math)

class Person:
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"Hello! My name is {self.name}.")

class Teacher(Person):
    def __init__(self, name, subject):
        super().__init__(name)
        self.subject = subject  
        

    def teach(self):
        print(f"{self.name} is teaching.")

teacher1 = Teacher("Ms. Cruz", "Mathematics")

class Board:
    def __init__(self, color):
        self.color = color

class Classroom:
    def __init__(self):
        self.board = Board("White")

class Laptop:
    def __init__(self, brand):
        self.brand = brand


class Lab:
    def __init__(self, laptop):
        self.laptop = laptop

class Thermometer:
    def measure(self):
        print("Temperature measured.")

class Scientist:
    def conduct_experiment(self, thermometer):
        thermometer.measure()

