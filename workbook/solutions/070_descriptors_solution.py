# Hints:
# - Descriptor __set__ can validate type of value before setting on instance.

# Solution:
class Typed:
    def __init__(self, name, typ):
        self.name = name
        self.typ = typ
    def __get__(self, instance, owner):
        return instance.__dict__.get(self.name)
    def __set__(self, instance, value):
        if not isinstance(value, self.typ):
            raise TypeError(f'Expected {self.typ}')
        instance.__dict__[self.name] = value

class C:
    age = Typed('age', int)

c = C()
c.age = 30
print(c.age)
