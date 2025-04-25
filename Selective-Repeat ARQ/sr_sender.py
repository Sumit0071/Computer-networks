# sr_sender.py
import socket
import time
import threading

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.settimeout(1)
server_addr = ('localhost', 9999)

frames = [f"frame{i}" for i in range(6)]
ack_received = [False] * len(frames)
window_size = 3

def receive_acks():
    while not all(ack_received):
        try:
            ack, _ = client.recvfrom(1024)
            ack_num = int(ack.decode()[3:])
            print(f"Received {ack.decode()}")
            ack_received[ack_num] = True
        except:
            continue

threading.Thread(target=receive_acks, daemon=True).start()

i = 0
while not all(ack_received):
    for j in range(window_size):
        index = i + j
        if index < len(frames) and not ack_received[index]:
            print(f"Sent: {frames[index]}")
            client.sendto(frames[index].encode(), server_addr)
    time.sleep(3)
    i += window_size

client.sendto("end".encode(), server_addr)
client.close()
