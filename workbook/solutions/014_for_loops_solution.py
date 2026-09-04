# Hints:
# - Use a loop from 1..n to compute factorial.

# Solution:
def factorial(n):
    res = 1
    for i in range(1, n+1):
        res *= i
    return res

print(factorial(5))
