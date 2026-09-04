# Hints:
# - Use subprocess.run with capture_output=True and check=True to get output safely.

# Solution:
import subprocess

def run_and_capture(cmd):
    res = subprocess.run(cmd, capture_output=True, text=True)
    return res.stdout

print(run_and_capture(['echo', 'hello']))
