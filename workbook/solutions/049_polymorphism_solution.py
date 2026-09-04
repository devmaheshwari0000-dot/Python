# Hints:
# - Two different classes implement same named method; call via a function.

# Solution:
class Dog:
    def speak(self):
        return 'woof'
class Cat:
    def speak(self):
        return 'meow'

def make_speak(animal):
    print(animal.speak())

make_speak(Dog())
make_speak(Cat())
