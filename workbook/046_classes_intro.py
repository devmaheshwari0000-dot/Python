# Example 46: Classes and objects (OOP intro)
# Topics: class, __init__, methods
class Dog:
    def __init__(self, name):
        self.name = name
    def bark(self):
        print(self.name + ' says woof')

d = Dog('Rex')
d.bark()

# Task: create a Cat class with meow() and a 'lives' attribute
