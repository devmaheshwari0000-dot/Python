# Hints:
# - Implement simple methods in class, use attributes.

# Solution:
class Cat:
    def __init__(self, name, lives=9):
        self.name = name
        self.lives = lives
    def meow(self):
        print(f"{self.name} says meow")

c = Cat('Mittens')
c.meow()
print('Lives:', c.lives)
