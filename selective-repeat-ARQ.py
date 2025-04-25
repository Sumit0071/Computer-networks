import random
def selective_repeat(frames, window_size):
    acked = [False] * len(frames)
    i = 0

    while not all(acked):
        for j in range(i, min(i + window_size, len(frames))):
            if not acked[j]:
                print(f"Sending Frame {j}: {frames[j]}")
        for j in range(i, min(i + window_size, len(frames))):
            if not acked[j]:
                if random.choice([True, False]):
                    print(f"ACK received for Frame {j}")
                    acked[j] = True
                else:
                    print(f"NACK for Frame {j}")
        while i < len(frames) and acked[i]:
            i += 1

frames = ['A', 'B', 'C', 'D', 'E']
selective_repeat(frames, 3)
