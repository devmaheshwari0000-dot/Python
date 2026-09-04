# Hints:
# - sys.argv[1:] contains CLI args as strings; convert to int before summing.

# Solution:
import sys

def sum_args(argv):
    nums = [int(x) for x in argv]
    return sum(nums)

# Example (simulate argv):
print(sum_args(['1','2','3']))
