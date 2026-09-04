# Hints:
# - Use zoneinfo.ZoneInfo to attach tzinfo to datetime and convert via astimezone().

# Solution:
from datetime import datetime
try:
    from zoneinfo import ZoneInfo
    now_utc = datetime.now(ZoneInfo('UTC'))
    local = now_utc.astimezone()
    print('UTC:', now_utc, 'Local:', local)
except Exception:
    print('zoneinfo not available')
