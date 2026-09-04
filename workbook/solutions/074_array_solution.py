# Hints:
# - array('f', ...) stores floats compactly.

# Solution:
from array import array
arr = array('f', [1.0, 2.0, 3.0])
mean = sum(arr) / len(arr)
print(mean)
