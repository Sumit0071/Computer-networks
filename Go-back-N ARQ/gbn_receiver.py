# gbn_receiver.py
import socket
import random

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind(('localhost', 9999))

expected_frame = 0
print("Receiver is ready (Go-Back-N)...")

while True:
    data, addr = server.recvfrom(1024)
    frame = data.decode()

    if frame == "end":
        print("Transmission ended.")
        break

    frame_num = int(frame[-1])

    if frame_num == expected_frame:
        print(f"Received expected frame: {frame}")
        if random.random() > 0.2:
            server.sendto(f"ACK{frame_num}".encode(), addr)
            print(f"Sent ACK{frame_num}\n")
        else:
            print("Simulated ACK loss\n")
        expected_frame += 1
    else:
        print(f"Discarded frame: {frame} (expected: {expected_frame})")
        if random.random() > 0.2:
            server.sendto(f"ACK{expected_frame - 1}".encode(), addr)
