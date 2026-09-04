# Example 40: Working with dates and times
# Topics: datetime
from datetime import datetime, timedelta
now = datetime.now()
print('Now:', now)
print('Tomorrow:', now + timedelta(days=1))

# Task: compute how many days until next New Year
