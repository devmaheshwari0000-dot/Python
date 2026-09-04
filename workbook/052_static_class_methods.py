# Example 52: Static and class methods
# Topics: @staticmethod, @classmethod
class MyClass:
    count = 0
    def __init__(self):
        MyClass.count += 1
    @staticmethod
    def hello():
        print('hello')
    @classmethod
    def how_many(cls):
        return cls.count

MyClass.hello()
print(MyClass.how_many())

# Task: use classmethod to create alternate constructors
