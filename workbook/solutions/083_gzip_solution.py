# Hints:
# - gzip.open reads/writes compressed files; decode bytes to string.

# Solution:
import gzip

def write_gzip(path, data: bytes):
    with gzip.open(path, 'wb') as f:
        f.write(data)

def read_gzip_first_line(path):
    with gzip.open(path, 'rb') as f:
        return f.readline().decode()

# write_gzip('/tmp/g.txt.gz', b'hello\nworld')
# print(read_gzip_first_line('/tmp/g.txt.gz'))
print('gzip example ready')
