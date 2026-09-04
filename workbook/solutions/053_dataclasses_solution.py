# Hints:
# - Dataclasses provide automatic repr and init.

# Solution:
from dataclasses import dataclass
import math

@dataclass
class Point:
    x: int
    y: int
    def dist_origin(self):
        return math.hypot(self.x, self.y)

p = Point(3,4)
print(p, p.dist_origin())
