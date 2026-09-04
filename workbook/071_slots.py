# Example 71: __slots__ to save memory
# Topics: __slots__
class Point:
    __slots__ = ('x','y')
    def __init__(self, x, y):
        self.x = x; self.y = y

p = Point(1,2)
print(p.x, p.y)

# Task: compare hasattr for __dict__ presence between classes with and without __slots__
