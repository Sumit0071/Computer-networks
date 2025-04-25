import random

def go_back_n(frames, window_size):
    i = 0
    while i < len(frames):
        end = min(i + window_size, len(frames))
        print(f"Sending window: {frames[i:end]}")
        acks = [random.choice([True, False]) for _ in frames[i:end]]

        if all(acks):
            print("All ACKs received.")
            i += window_size
        else:
            error_index = i + acks.index(False)
            print(f"NACK for Frame {error_index}, resending from Frame {error_index}")
            i = error_index

frames = ['A', 'B', 'C', 'D', 'E', 'F']
go_back_n(frames, 3)
