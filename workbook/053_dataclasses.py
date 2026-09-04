# Example 53: dataclasses
# Topics: dataclasses.dataclass
from dataclasses import dataclass

@dataclass
class Point:
    x: int
    y: int

p = Point(2,3)
print(p)

# Task: add a method to dataclass that computes distance to origin
