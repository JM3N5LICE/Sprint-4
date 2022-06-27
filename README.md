
# Overview


This project may seem simple but i did this to gain a basic understanding of how networks work. 

In this TCP echo network I wanted to make a simple project that connects on a network where the client sends a key word and if it is in the server's dictionary it will return the value associated with the key over the network connection. 


[Software Demo Video](http://youtu.be/h29I3OBxHSU?hd=1)

# Network Communication


I used a client to server connection. It is a TCP connection using the port number 65432 and the IP address "127.0.0.1".
The formatof the messages being sent are strings being encoded to packets and then being coded back into strings.

# Development Environment

This project is written completely in Python in the VSCode app using the socket library.
# Useful Websites

* [Socket Programming Python Tutorial](https://realpython.com/python-sockets/)
* [Python Socket Server Library](https://docs.python.org/3/library/socketserver.html)

# Future Work

* Server continues to listen after client disconnects.
* A GUI for the client side
* Client can add and modify dictionary on server side from client.
