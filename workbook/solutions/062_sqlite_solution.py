# Hints:
# - Use sqlite3 to create table and use SUM()/COUNT() for aggregates.

# Solution:
import sqlite3
con = sqlite3.connect(':memory:')
cur = con.cursor()
cur.execute('CREATE TABLE items(amount INT)')
cur.executemany('INSERT INTO items VALUES (?)', [(10,),(20,),(30,)])
cur.execute('SELECT SUM(amount) FROM items')
print(cur.fetchone()[0])
con.close()
