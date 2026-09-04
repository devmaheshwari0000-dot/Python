# Example 18: Lambda functions
# Topics: anonymous functions, key parameter
add = lambda a, b: a + b
print(add(3, 4))
pairs = [(1, 'a'), (3, 'b'), (2, 'c')]
print(sorted(pairs, key=lambda p: p[0]))

# Task: use lambda with map to square numbers
