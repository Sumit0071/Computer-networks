# sr_receiver.py
import socket
import random

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('localhost', 9999))

received_frames = {}
expected = 0
window_size = 3

print("Receiver is ready (Selective Repeat)...")

while True:
    data, addr = server.recvfrom(1024)
    frame = data.decode()

    if frame == "end":
        print("Transmission ended.")
        break

    seq = int(frame[-1])
    print(f"Received: {frame}")

    if seq not in received_frames:
        received_frames[seq] = frame
        if random.random() > 0.2:
            server.sendto(f"ACK{seq}".encode(), addr)
            print(f"Sent ACK{seq}\n")
        else:
            print("Simulated ACK loss\n")

    while expected in received_frames:
        print(f"Delivered: {received_frames[expected]}")
        expected += 1
