# Hints:
# - Use super() to call base class methods when overriding.

# Solution:
class Animal:
    def speak(self):
        return '...'

class Bird(Animal):
    def speak(self):
        return 'tweet'

print(Bird().speak())
