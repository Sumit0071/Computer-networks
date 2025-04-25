# udp_client.py
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.sendto("Hello UDP Server".encode(), ('localhost', 9999))
data, _ = client.recvfrom(1024)
print("Server says:", data.decode())

client.close()
