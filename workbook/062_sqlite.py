# Example 62: SQLite basic usage
# Topics: sqlite3
import sqlite3
con = sqlite3.connect(':memory:')
cur = con.cursor()
cur.execute('CREATE TABLE t(x INT)')
cur.execute('INSERT INTO t VALUES (1)')
print(list(cur.execute('SELECT * FROM t')))

# Task: create a table, insert rows, query aggregate
