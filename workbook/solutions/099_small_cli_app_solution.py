# Hints:
# - A tiny todo CLI needs add (append to file) and list (read file) commands.

# Solution:
import argparse

def add_todo(path, text):
    with open(path, 'a') as f:
        f.write(text + '\n')

def list_todos(path):
    with open(path) as f:
        return [line.strip() for line in f]

# Example usage (not parsing real argv here):
path = '/tmp/todos.txt'
add_todo(path, 'Buy milk')
print(list_todos(path))
