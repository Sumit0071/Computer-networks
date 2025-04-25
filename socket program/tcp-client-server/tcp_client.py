# Import socket module
import socket
# Create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Get local machine name
host = socket.gethostname()

# Define the port on which we want to connect
port = 23456

# connect to the server on local computer
s.connect((host, port))
# Receive data from the server
msg = s.recv(1024).decode('utf-8')
print (msg)
# Close the connection
s.close()