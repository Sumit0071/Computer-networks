# udp_server.py
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('localhost', 9999))
print("UDP Server is up...")

while True:
    data, addr = server.recvfrom(1024)
    print("Message from client:", data.decode())
    server.sendto("Ack from server".encode(), addr)
