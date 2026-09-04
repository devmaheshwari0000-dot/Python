# Example 54: Typing hints
# Topics: type annotations, Optional
from typing import List, Optional

def greet_all(names: List[str]) -> None:
    for n in names:
        print('Hello', n)

# Task: annotate a function that returns Optional[int]
