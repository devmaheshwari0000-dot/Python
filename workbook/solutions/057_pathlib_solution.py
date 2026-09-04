# Hints:
# - Path.rglob('*.py') lists .py files recursively.

# Solution:
from pathlib import Path

def list_py_files(dir_path):
    p = Path(dir_path)
    return [str(x) for x in p.rglob('*.py')]

print(list_py_files('.'))
