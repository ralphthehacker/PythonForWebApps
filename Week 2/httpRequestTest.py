import socket
import urllib3
#method 1
#Creates a socket that is connected to the internet, streaming data
my_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
my_socket.connect(('www.py4inf.com',80))

#Sending the request
my_socket.send('GET http://www.py4inf.com/code/intro-short.txt HTTP/1.0\n\n'.encode())

# Receives data from the socket and prints it until it receives a invalid message(len==1)
while True:
    data = my_socket.recv(512).decode()
    if len(data)<1:
        break
    print(data)

# Closes the socket

my_socket.close()

