# Hints:
# - Use class attribute for counting instances; provide a safe decrement method.

# Solution:
class Counter:
    instances = 0
    def __init__(self):
        Counter.instances += 1
    def destroy(self):
        if Counter.instances > 0:
            Counter.instances -= 1

c1 = Counter(); c2 = Counter()
print(Counter.instances)
c1.destroy()
print(Counter.instances)
