# Example 55: Enums
# Topics: enum.Enum
from enum import Enum
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

print(Color.RED, Color.RED.name, Color.RED.value)

# Task: use Enum to represent order statuses
