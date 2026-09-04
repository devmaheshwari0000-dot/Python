# Hints:
# - Use Enum members for statuses and compare by identity or .name/

# Solution:
from enum import Enum
class OrderStatus(Enum):
    PENDING = 'pending'
    SHIPPED = 'shipped'
    CANCELLED = 'cancelled'

print(OrderStatus.PENDING, OrderStatus.PENDING.value)
