# Hints:
# - Use contextlib.contextmanager decorator to create generator-style context managers.

# Solution:
from contextlib import contextmanager
import logging

@contextmanager
def log_exceptions(name):
    try:
        yield
    except Exception as e:
        logging.exception(f"Exception in {name}: {e}")
        raise

# Usage example:
# with log_exceptions('myblock'):
#     raise RuntimeError('boom')
print('contextmanager example defined')
