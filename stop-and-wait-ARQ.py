import time
import random

def stop_and_wait_arq(data):
    for i, frame in enumerate(data):
        print(f"Sending Frame {i}: {frame}")
        time.sleep(1)
        if random.choice([True, False]):
            print(f"ACK received for Frame {i}")
        else:
            print(f"Timeout for Frame {i}, resending...")
            time.sleep(1)
            print(f"Resent Frame {i}: {frame}")
            print(f"ACK received for Frame {i}")

frames = ['A', 'B', 'C', 'D']
stop_and_wait_arq(frames)
