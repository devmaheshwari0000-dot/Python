# Example 39: CSV reading and writing
# Topics: csv module
import csv
rows = [['name','age'], ['Ann','30'], ['Ben','25']]
with open('/tmp/test.csv', 'w', newline='') as f:
    w = csv.writer(f)
    w.writerows(rows)

# Task: read back the CSV and store as list of dicts
