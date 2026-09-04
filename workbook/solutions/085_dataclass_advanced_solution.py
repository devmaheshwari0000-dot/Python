# Hints:
# - frozen dataclasses prevent attribute assignment after creation; default_factory for mutable defaults.

# Solution:
from dataclasses import dataclass, field

@dataclass(frozen=True)
class ImmutablePoint:
    x: int
    y: int

@dataclass
class Bag:
    items: list = field(default_factory=list)

b = Bag()
b.items.append(1)
print(ImmutablePoint(1,2), b)
