import socket
import sys

UDP_IP_ADDRESS = "127.0.0.1"
UDP_PORT_NO = int(sys.argv[1])

Message = str.encode("Hello, server")

clientSock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

clientSock.sendto(Message, (UDP_IP_ADDRESS, UDP_PORT_NO))

