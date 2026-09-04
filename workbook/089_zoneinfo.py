# Example 89: Working with timezones (zoneinfo)
# Topics: zoneinfo (Python 3.9+)
from datetime import datetime
try:
    from zoneinfo import ZoneInfo
    now = datetime.now(ZoneInfo('UTC'))
    print(now)
except Exception:
    print('zoneinfo not available')

# Task: convert UTC time to local timezone
