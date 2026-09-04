# Hints:
# - __slots__ removes __dict__ and saves memory.

# Solution:
class PointSlots:
    __slots__ = ('x','y')
    def __init__(self, x, y):
        self.x = x; self.y = y

p = PointSlots(1,2)
print(hasattr(p, '__dict__'))
