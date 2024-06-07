# Create a class Person with instance attributes name and age. Create a method get_details in this class to print name and age.

class Person:
    def __init__(self, name, age):
        self.name = name  # p.name = Jane   p.age = 30
        self.age = age

    def get_details(self):
        return f"Name of the student is {self.name} and age of the student is {self.age}"


p = Person("Jane", 30)
print(p.get_details())  # None