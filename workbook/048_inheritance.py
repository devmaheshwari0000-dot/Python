# Example 48: Inheritance
# Topics: subclassing, super()
class Animal:
    def speak(self):
        print('...')

class Dog(Animal):
    def speak(self):
        super().speak()
        print('woof')

Dog().speak()

# Task: create a Bird class inheriting Animal and override speak
