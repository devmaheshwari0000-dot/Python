# Example 50: Encapsulation and property
# Topics: private attributes (convention), @property
class Person:
    def __init__(self, age):
        self._age = age
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        if value < 0: raise ValueError('age cannot be negative')
        self._age = value

p = Person(20)
print(p.age)

# Task: protect an attribute and validate in setter
