# Hints:
# - Use secrets.choice over random for secure selection.

# Solution:
import secrets
import string

def gen_password(length=12):
    alphabet = string.ascii_letters + string.digits
    return ''.join(secrets.choice(alphabet) for _ in range(length))

print(gen_password(12))
