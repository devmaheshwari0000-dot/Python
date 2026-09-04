# Hints:
# - UDP uses SOCK_DGRAM; server listens on recvfrom.

# Solution:
# Example code (not started here):
import socket

def udp_echo_server(host='127.0.0.1', port=9999):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.bind((host, port))
    data, addr = s.recvfrom(1024)
    s.sendto(data, addr)
    s.close()

print('UDP example defined')
