class Student:
        def __init__(self, name):
            self.name = name

class School:
        def __init__(self, name):
            self.name = name
            self.students = []

        def add_student(self, student):
            self.students.append(student)

class Teacher:
    def __init__(self, name):
        self.name = name
        self.students= []

    def add_student(self, student):
        self.students.append(student)

        

        
school = School("Riverside High")
s1 = Student("Ana")
s2 = Student("Ben")
school.add_student(s1)
school.add_student(s2)
print(f"School: {school.name}")
print(f"Student 1: {s1.name}")
print(f"Student 2: {s2.name}")