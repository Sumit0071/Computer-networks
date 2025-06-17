import socket

def calculate_parity(data_bits):
    m = len(data_bits)
    r = 0
    # Find number of parity bits
    while (2 ** r) < (m + r + 1):
        r += 1

    total_bits = m + r
    hamming = ['0'] * total_bits

    j = 0
    for i in range(1, total_bits + 1):
        if (i & (i - 1)) == 0:  # power of two, parity bit
            continue
        hamming[i - 1] = data_bits[j]
        j += 1

    for i in range(r):
        parity_pos = 2 ** i
        parity = 0
        for j in range(1, total_bits + 1):
            if j & parity_pos and j != parity_pos:
                parity ^= int(hamming[j - 1])
        hamming[parity_pos - 1] = str(parity)

    return ''.join(hamming)

def start_client(host='localhost', port=12345):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    data = input("Enter binary data (e.g. 1011): ").strip()
    encoded = calculate_parity(data)
    print(f"[>] Sending Hamming encoded data: {encoded}")

    s.send(encoded.encode())
    s.close()

if __name__ == "__main__":
    start_client()
