# Exercise: Colleague, a subclass of Person
# 1. Extend Person with a Colleague subclass
#     - The constructor should accept an additional 'office_location' parameter.
# 2. How would we deal with someone who is both a Colleague and a Friend?

class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

class Colleague(Person):
    def __init__(self, name, age, gender, office_location):
        super().__init__(name, age, gender)
        self.office_location = office_location


jd = Colleague("Jane Doe", 28, 'Female', "San Francisco HQ")