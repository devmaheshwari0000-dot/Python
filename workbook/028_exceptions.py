# Example 28: Exception handling
# Topics: try, except, finally, raise
try:
    x = int('notanint')
except ValueError as e:
    print('Caught ValueError:', e)
finally:
    print('Done')

# Task: write a function that raises ValueError for negative input
