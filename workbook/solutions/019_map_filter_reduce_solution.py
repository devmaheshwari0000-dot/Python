# Hints:
# - Use functools.reduce to accumulate product.

# Solution:
from functools import reduce
from operator import mul

nums = [1,2,3,4]
product = reduce(mul, nums, 1)
print(product)
