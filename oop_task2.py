"""
Create a class SchoolMember that represents any person in school. Classes Teacher and Student are inherited from SchoolMember.
Classes should have the same interface as the public show () method. Teacher accepts name (str), age (int), and salary (int).
Student accepts name (str), age (int), and grades. Move the same logic of initialization to the class SchoolMember.
Method show() returns a string (see string patterns in the Example).
All attributes that were accepted should be public.
"""


class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def show(self):
        return f"Name: {self.name}, Age: {self.age}"


class Teacher(SchoolMember):
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary

    def show(self):
        r = SchoolMember.show(self)
        return r+f", Salary: {self.salary}"


class Student(SchoolMember):
    def __init__(self, name, age, grades):
        SchoolMember.__init__(self, name, age)
        self.grades = grades

    def show(self):
        r = SchoolMember.show(self)
        return r+f", Grades: {self.grades}"


harry = Student("Harry", 8, 55)
print(harry.show())

snape = Teacher("Snape", 75, 1000)
print(snape.show())
