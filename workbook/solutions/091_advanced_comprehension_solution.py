# Hints:
# - Nested comprehensions: [[i*j for j in range(1,n+1)] for i in range(1,m+1)]

# Solution:
m = 5
n = 5
mult_table = [[i*j for j in range(1, n+1)] for i in range(1, m+1)]
print(mult_table)
