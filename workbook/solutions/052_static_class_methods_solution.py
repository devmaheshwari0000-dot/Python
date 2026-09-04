# Hints:
# - @staticmethod doesn't receive cls or self; @classmethod receives cls.

# Solution:
class MyClass:
    count = 0
    def __init__(self):
        MyClass.count += 1
    @staticmethod
    def hello():
        return 'hello'
    @classmethod
    def how_many(cls):
        return cls.count

print(MyClass.hello())
print(MyClass.how_many())
