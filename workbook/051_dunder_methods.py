# Example 51: Magic/Dunder methods
# Topics: __str__, __repr__, __len__
class Box:
    def __init__(self, items):
        self.items = list(items)
    def __len__(self):
        return len(self.items)
    def __str__(self):
        return 'Box(' + ','.join(map(str,self.items)) + ')'

b = Box([1,2,3])
print(len(b), b)

# Task: implement __add__ to combine two Box objects
