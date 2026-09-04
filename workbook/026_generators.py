# Example 26: Generators and yield
# Topics: yield, generator functions
def count_up_to(n):
    i = 1
    while i <= n:
        yield i
        i += 1

for num in count_up_to(5):
    print(num)

# Task: write a generator that yields prime numbers
