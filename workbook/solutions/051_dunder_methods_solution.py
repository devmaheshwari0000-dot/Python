# Hints:
# - Implement __add__ to return a new Box with combined items.

# Solution:
class Box:
    def __init__(self, items):
        self.items = list(items)
    def __len__(self):
        return len(self.items)
    def __str__(self):
        return 'Box(' + ','.join(map(str,self.items)) + ')'
    def __add__(self, other):
        return Box(self.items + other.items)

b1 = Box([1,2])
b2 = Box([3])
print((b1 + b2))
