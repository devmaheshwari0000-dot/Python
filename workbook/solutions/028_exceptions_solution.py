# Hints:
# - Raise ValueError for negatives.

# Solution:
def check_positive(n):
    if n < 0:
        raise ValueError('negative not allowed')
    return True

try:
    check_positive(-1)
except ValueError as e:
    print('Caught:', e)
