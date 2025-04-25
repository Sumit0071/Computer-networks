import socket
import threading

clients = {}  # socket: address

def handle_client(client_socket, addr):
    while True:
        try:
            msg = client_socket.recv(1024).decode()
            if msg:
                print(f"Received from {addr}: {msg}")
                broadcast_msg = f"{addr}: {msg}"
                for c in clients:
                    if c != client_socket:
                        c.send(broadcast_msg.encode())
        except:
            print(f"Client {addr} disconnected.")
            client_socket.close()
            del clients[client_socket]
            break

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9999))
server.listen(5)
print("Multi-client server started...")

while True:
    client_socket, addr = server.accept()
    clients[client_socket] = addr
    print(f"Client {addr} connected.")
    threading.Thread(target=handle_client, args=(client_socket, addr)).start()
