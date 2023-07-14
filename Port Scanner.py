import socket
import sys

hostipaddress = input("Enter host or website public ip address to scan now: ")

try:
    for port in range(21,60):
        sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        sock.settimeout(5)
        result = sock.connect_ex((hostipaddress,port))
        if result == 0:
            print("Port  {}:\t Open".format(port))
        else:
            print("Port  {}:\t Closed".format(port))
        sock.close()
except socket.error as se:
    print("Could not establish a connection! "+str(se))
    sys.exit()


