# Example 49: Polymorphism
# Topics: duck typing, common interface
class A:
    def run(self): print('A')
class B:
    def run(self): print('B')

def call_run(x):
    x.run()

call_run(A()); call_run(B())

# Task: show polymorphism with different classes implementing same method
