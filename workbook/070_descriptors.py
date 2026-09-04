# Example 70: Descriptors
# Topics: descriptor protocol (__get__, __set__)
class Descriptor:
    def __init__(self): self._value = None
    def __get__(self, instance, owner):
        return self._value
    def __set__(self, instance, value):
        self._value = value

class C:
    attr = Descriptor()

c = C(); c.attr = 5
print(c.attr)

# Task: implement a descriptor that enforces a type for the attribute
