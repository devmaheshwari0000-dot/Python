# Hints:
# - platform.architecture()[0] gives '64bit' or '32bit'.

# Solution:
import platform
bits = platform.architecture()[0]
print('Interpreter architecture:', bits)
