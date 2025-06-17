import socket
import random

def detect_and_correct(data):
    n = len(data)
    data = list(map(int, data))
    error_pos = 0

    # Calculate parity bits positions (powers of 2)
    for i in range(n):
        if (i + 1) & (i) == 0:  # parity bits
            parity = 0
            for j in range(i, n):
                if ((j + 1) & (i + 1)) != 0:
                    parity ^= data[j]
            if parity != 0:
                error_pos += (i + 1)

    if error_pos > 0:
        print(f"[!] Error detected at bit position: {error_pos}")
        data[error_pos - 1] ^= 1  # Flip the erroneous bit
    else:
        print("[✓] No error detected")

    return ''.join(map(str, data)), error_pos

def start_server(host='localhost', port=12345):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    print(f"[+] Server listening on {host}:{port}")

    conn, addr = s.accept()
    print(f"[+] Connected by {addr}")

    received = conn.recv(1024).decode()
    if not received:
        print("[-] No data received. Closing connection.")
        conn.close()
        return

    print(f"[>] Received Hamming data: {received}")

    # Step 1: Check if data already has an error
    print("\n[~] Checking received data for errors...")
    corrected_data, error_pos = detect_and_correct(received)
    if error_pos > 0:
        print(f"[!] Received data was already corrupted at bit position {error_pos}.")
        print(f"[✔] Corrected original data: {corrected_data}")
    else:
        print("[✓] Received data is clean. Now simulating error...\n")

        # Step 2: Simulate error
        data = list(received)
        error_index = random.randint(0, len(data) - 1)
        data[error_index] = '1' if data[error_index] == '0' else '0'
        errored_data = ''.join(data)
        print(f"[x] Simulated error at bit {error_index + 1}: {errored_data}")

        # Step 3: Correct the simulated error
        corrected_data, error_pos = detect_and_correct(errored_data)
        print(f"[✔] Corrected simulated error data: {corrected_data}")

    conn.close()

if __name__ == "__main__":
    start_server()
