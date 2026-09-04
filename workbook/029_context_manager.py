# Example 29: Context managers and with
# Topics: __enter__, __exit__, with statement
with open('/tmp/example.txt', 'w') as f:
    f.write('hello')

# Task: create a simple context manager class that times a block
