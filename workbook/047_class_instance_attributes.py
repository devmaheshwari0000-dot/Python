# Example 47: Instance and class attributes
# Topics: class vs instance attributes
class Counter:
    instances = 0
    def __init__(self):
        Counter.instances += 1

c1 = Counter(); c2 = Counter()
print(Counter.instances)

# Task: add a method to decrement instances safely
