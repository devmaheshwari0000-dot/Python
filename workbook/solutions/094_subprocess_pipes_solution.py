# Hints:
# - Use Popen and iterate over stdout lines (text=True) to stream output.

# Solution:
import subprocess

def stream_cmd(cmd):
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, text=True)
    for line in p.stdout:
        print('OUT:', line.rstrip())
    p.wait()

# Example commented: stream_cmd(['ping','-c','3','127.0.0.1'])
print('subprocess streaming example defined')
