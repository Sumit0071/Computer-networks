# sender.py
import socket
import time

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client.settimeout(3)

server_addr = ('localhost', 9999)

frames = ['frame1', 'frame2', 'frame3', 'frame4']

for frame in frames:
    while True:
        client.sendto(frame.encode(), server_addr)
        print(f"Sent: {frame}")

        try:
            ack, _ = client.recvfrom(1024)
            if ack.decode() == "ACK":
                print("Received: ACK\n")
                break
        except socket.timeout:
            print("ACK not received, retransmitting...\n")

# End of transmission
client.sendto("end".encode(), server_addr)
client.close()
