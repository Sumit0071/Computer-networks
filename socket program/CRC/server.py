import socket

# Include the CRC helper functions here...
from crc_utils import mod2div

def start_server(host='localhost', port=12345):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((host, port))
    s.listen(1)
    print(f"[+] Server listening on {host}:{port}")

    conn, addr = s.accept()
    print(f"[+] Connected by {addr}")

    received = conn.recv(1024).decode()
    if not received:
        print("[-] No data received.")
        conn.close()
        return

    encoded_data, key = received.split('|')
    print(f"[>] Received data: {encoded_data}")
    print(f"[>] Generator key: {key}")

    remainder = mod2div(encoded_data, key)
    print(f"[~] Remainder after division: {remainder}")

    if '1' in remainder:
        print("[!] Error detected in received data!")
    else:
        print("[✓] No error detected in received data.")

    conn.close()

if __name__ == "__main__":
    start_server()
