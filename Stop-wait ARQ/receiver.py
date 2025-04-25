# receiver.py
import socket
import random
import time

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('localhost', 9999))

print("Receiver ready to receive...")

while True:
    data, addr = server.recvfrom(1024)
    frame = data.decode()

    if frame == "end":
        print("Transmission ended.")
        break

    print(f"Received: {frame}")

    # Simulate random packet loss (ACK loss)
    if random.random() > 0.2:  # 80% chance to ACK
        time.sleep(1)
        server.sendto("ACK".encode(), addr)
        print("Sent: ACK")
    else:
        print("ACK lost (simulated)")
