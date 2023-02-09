# Nicolette Thiro, Nishat Ahmed, Armaan Kapoor - CLI Client

import http.client
import os
import sys

#make CLI arguments so that the program can be invoked using python http_client.py <server_ip> <port> <path>

server_ip = sys.argv[1] # get the server ip from the first argument
port = sys.argv[2] # get the port from the second argument
path = sys.argv[3] # get the path from the third argument

conn = http.client.HTTPConnection(server_ip, port) 
conn.request("GET", path) 

response = conn.getresponse() 

if response.status == 200: # if the response status is 200 OK
    data = response.read() 
    print("Files received successfully.\n\nContents: ") 
    print(data.decode()) # print the file contents
else:
    print("Error retrieving file") # print an error message if the response status is not 200 OK