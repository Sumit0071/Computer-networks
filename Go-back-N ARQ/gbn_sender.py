# gbn_sender.py
import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.settimeout(3)

server_addr = ('localhost', 9999)

frames = [f"frame{i}" for i in range(6)]
window_size = 3
base = 0
next_seq = 0

print("Sender started (Go-Back-N)...\n")

while base < len(frames):
    while next_seq < base + window_size and next_seq < len(frames):
        client.sendto(frames[next_seq].encode(), server_addr)
        print(f"Sent: {frames[next_seq]}")
        next_seq += 1

    try:
        ack_data, _ = client.recvfrom(1024)
        ack_num = int(ack_data.decode()[3:])
        print(f"Received: {ack_data.decode()}\n")
        base = ack_num + 1
    except socket.timeout:
        print("Timeout! Resending window...\n")
        next_seq = base  # Go back

client.sendto("end".encode(), server_addr)
client.close()
