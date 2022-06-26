# echo-client.py

import socket

HOST = "127.0.0.1"  # The server's hostname or IP address
PORT = 65432  # The port used by the server

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    # connect() is the command for the socket object to connect to the server and calls the sendall() to send its message
    s.connect((HOST, PORT))  
    message = input("Type a name in the dictionary: ")
    s.sendall(str.encode(message))
    # recv reads the servers reply and prints it
    data = s.recv(1024)
    # This means our socket is going to attempt to receive data, in a buffer size of 1024 bytes at a time. From what I can tell, computers use this number because 
    # it is a power of 2 to the 10th power.

print(f"Received {data.decode('utf-8')!r}")

# Run server shell command: python echo-client.py