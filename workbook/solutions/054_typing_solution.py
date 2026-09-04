# Hints:
# - Annotate parameters and return types; Optional is used for None return.

# Solution:
from typing import List, Optional

def find_first_even(nums: List[int]) -> Optional[int]:
    for n in nums:
        if n % 2 == 0:
            return n
    return None

print(find_first_even([1,3,4,5]))
