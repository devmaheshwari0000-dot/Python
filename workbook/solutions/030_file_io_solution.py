# Hints:
# - Use with open(...) as f for safe file handling.

# Solution:
def copy_file(src, dst):
    with open(src, 'r') as fr, open(dst, 'w') as fw:
        for line in fr:
            fw.write(line)

# Example usage commented out for safety
# copy_file('/tmp/example2.txt', '/tmp/example2_copy.txt')
