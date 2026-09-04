# Example 30: File I/O reading and writing
# Topics: open, read, write, modes
with open('/tmp/example2.txt', 'w') as f:
    f.write('line1\nline2')
with open('/tmp/example2.txt') as f:
    data = f.read()
print(data)

# Task: write a function to copy a file line-by-line
