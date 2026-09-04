# Hints:
# - Write simple server using socket.socket and bind/listen/accept; be careful in restricted envs.

# Solution:
# The following is example code; not executed in restricted environments.
import socket

def echo_server_example(host='127.0.0.1', port=50007):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    conn, addr = s.accept()
    with conn:
        data = conn.recv(1024)
        conn.sendall(data)
    s.close()

print('Echo server example defined (not started)')
