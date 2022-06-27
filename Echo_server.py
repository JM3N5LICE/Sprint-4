import socket

# Localhost is the default name of the computer you are working on. The term is a pseudo name for 127.0. 0.1, 
# the IP address of the local computer. This IP address allows the machine to connect to and communicate with itself.
HOST = "127.0.0.1"

# port represents the TCP port number to accept connections on from clients. It should be an integer from 1 to 65535, 
# as 0 is reserved. Some systems may require superuser privileges if the port number is less than 1024.
PORT = 65432

my_dictionary = {
    "Justyn" : "Mencl",
    "Bob" : "Marley",
    "Chad" : "Macbeth"
}

# socket.socket() creates a socket object that supports the context manager type, so you can use it in a with statement.

# The arguments passed to socket() are constants used to specify the address family and socket type. AF_INET is the 
# Internet address family for IPv4. SOCK_STREAM is the socket type for TCP, the protocol that will be used to transport 
# messages in the network.
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #The .bind() method is used to associate the socket with a specific network interface and port number
    # s refers to the socket object we are manipulating.
    
    s.bind((HOST, PORT))

    #The listen() command listens for connections for clients
    s.listen()

    # accept() creates a new socket object that holds the address of the client
    #After .accept() provides the client socket object conn, an infinite while loop is used to loop over blocking calls to conn.recv(). 
    # This reads whatever data the client sends and echoes it back using conn.sendall().
    #If conn.recv() returns an empty bytes object, b'', that signals that the client closed the connection and the loop is terminated. 
    # The with statement is used with conn to automatically close the socket at the end of the block.
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        # while True:
        #     # client, addr = s.accept()
        while True:
            data = conn.recv(1024)
            try:
                value = my_dictionary.get(data.decode('utf-8'))
                if not data:
                    break
                conn.sendall(str.encode(value))
            except:
                if not data:
                    break
                conn.sendall(b"Invalid name")


# Run server shell command: python Echo_server.py

