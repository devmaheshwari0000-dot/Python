# Example 85: Data classes advanced (frozen, default_factory)
# Topics: dataclasses features
from dataclasses import dataclass, field
from typing import List

@dataclass(frozen=True)
class ImmutablePoint:
    x: int
    y: int

@dataclass
class Bag:
    items: List[int] = field(default_factory=list)

print(ImmutablePoint(1,2))

# Task: create a frozen dataclass and show that assignment fails
