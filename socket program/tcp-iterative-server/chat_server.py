# chat_server.py
import socket

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(('localhost', 9999))
server.listen(5)
print("Chat server started...")
conn, addr = server.accept()
print(f"Connected with {addr}")

while True:
    msg = conn.recv(1024).decode()
    if msg.lower() == 'exit':
        print("Client disconnected.")
        break
    print("Client:", msg)
    reply = input("You: ")
    conn.send(reply.encode())

conn.close()
