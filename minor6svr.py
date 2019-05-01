import socket
import random
import sys

UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = int(sys.argv[1])
message = str.encode("Hello, client")

serverSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serverSock.bind((UDP_IP_ADDRESS, UDP_PORT_NO))

print("UDP server up and listening...")

while True:
    data, addr = serverSock.recvfrom(1024)
    print("Message: ",data, "Address: ", addr)
    serverSock.sendto(message,addr)
