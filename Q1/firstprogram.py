class Dog:
    def __init__(self, name, age):
            self.name = name
            self.age = age

    def bark(self):
        print("Woof! Woof!")

    def display_info(self):
        print(f"Name: {self.name}, Age: {self.age}")


dog1 = Dog("Buddy", 3)
dog2 = Dog("Max", 5)

dog1.display_info()
dog1.bark()

dog2.display_info()
dog2.bark()
        
