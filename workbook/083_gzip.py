# Example 83: Working with compressed files
# Topics: gzip
import gzip
s = b'hello world'
with gzip.open('/tmp/g.txt.gz', 'wb') as f:
    f.write(s)

# Task: read a gzipped file and print first line
