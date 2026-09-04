# Hints:
# - Use @property and validation in setter.

# Solution:
class Person:
    def __init__(self, age):
        self._age = age
    @property
    def age(self):
        return self._age
    @age.setter
    def age(self, value):
        if value < 0:
            raise ValueError('age cannot be negative')
        self._age = value

p = Person(30)
try:
    p.age = -5
except ValueError as e:
    print('Validation:', e)
