# Hints:
# - Use while to generate Fibonacci until N.

# Solution:
def fib_up_to_n(n):
    a, b = 0, 1
    res = []
    while a <= n:
        res.append(a)
        a, b = b, a + b
    return res

print(fib_up_to_n(21))
