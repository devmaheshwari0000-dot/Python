# Example 25: Recursion basics
# Topics: recursive functions, base case
def factorial(n):
    if n <= 1:
        return 1
    return n * factorial(n-1)

print(factorial(5))

# Task: implement recursive Fibonacci (with base cases)
