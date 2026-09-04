# Hints:
# - Use argparse.ArgumentParser and add_argument with type.

# Solution:
import argparse

def make_parser(args=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=str, required=False)
    parser.add_argument('--output', type=str, required=False)
    return parser.parse_args(args)

print(make_parser(['--input', 'in.txt', '--output', 'out.txt']))
