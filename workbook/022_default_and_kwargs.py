# Example 22: Default arguments and keyword args
# Topics: default params, kwargs
def power(x, y=2):
    return x ** y

print(power(3))
print(power(2, 5))

# Task: write a function that accepts **kwargs and prints keys sorted
