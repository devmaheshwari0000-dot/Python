# Hints:
# - os.getenv with default; use open to write file.

# Solution:
import os

def write_in_cwd(filename, content):
    home = os.getenv('HOME', '.')
    path = os.path.join(os.getcwd(), filename)
    with open(path, 'w') as f:
        f.write(content)
    return path

print(write_in_cwd('example_out.txt', 'hello'))
