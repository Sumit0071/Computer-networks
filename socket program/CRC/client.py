import socket

# Include the CRC helper functions here...
from crc_utils import encode_data

def start_client(host='localhost', port=12345):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))

    data = input("Enter binary data: ").strip()
    key = input("Enter generator (e.g., 1101): ").strip()

    encoded_data = encode_data(data, key)
    print(f"[>] Encoded data to send: {encoded_data}")

    # Send both encoded data and key
    s.send(f"{encoded_data}|{key}".encode())
    s.close()

if __name__ == "__main__":
    start_client()
