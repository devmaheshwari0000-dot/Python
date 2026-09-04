# Hints:
# - Use datetime.today and compute delta to next Jan 1.

# Solution:
from datetime import datetime

def days_until_new_year():
    now = datetime.now()
    next_year = datetime(now.year + 1, 1, 1)
    delta = next_year - now
    return delta.days

print(days_until_new_year())
