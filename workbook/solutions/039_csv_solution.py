# Hints:
# - csv.DictReader produces dictionaries per row.

# Solution:
import csv

rows = [['name','age'], ['Ann','30'], ['Ben','25']]
with open('/tmp/test.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerows(rows)

with open('/tmp/test.csv', newline='') as f:
    reader = csv.DictReader(f)
    data = list(reader)
print(data)
