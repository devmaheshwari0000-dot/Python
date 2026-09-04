# Example 35: Using argparse for CLI
# Topics: argparse, options, help
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--count', type=int, default=1)
args = parser.parse_args([])  # empty for example
print('count =', args.count)

# Task: create a CLI that accepts --input and --output paths
