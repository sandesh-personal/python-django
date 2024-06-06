# return greater number from list using fliter function

data = [12, 10, 5, 6, 20, 15]

def get_greater_number(element):
    if element > 10:
        return True
    else:
        return False
# result = list(filter(get_greater_number, data))
result = list(filter(lambda x : x > 10, data))
print(result)


# lambda task 1
data = [1, 2, 3, 4, 5, 6, 7]

result = list(filter(lambda x : x % 2 == 0, data))
print(result)


# lambda task 2
from functools import reduce
data = [1, 2, 3, 4, 5]

result = reduce(lambda x, y: x * y, data)
print(result)


# oop task
# create a student class with instance attribute name and roll number 
# create classroom as class attribue and finally a methdod to get all his info and print all his information

class Student:
    subject = "Python Django"  # class attribute

    def __init__(self, name, roll_number):  # constructor
        self.name = name  # instance attribute
        self.roll_number = roll_number  # instance attribute

    def get_info(self):
        return f"name: {self.name} and roll number is: {self.roll_number} "

    

c1 = Student("sandesh", "1")

print(Student.subject)  # Python Django
print(c1.name)  # sandesh
print(c1.roll_number)  # 1

result = c1.get_info()
print(result)