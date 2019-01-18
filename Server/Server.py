# This code was typed out referencing a YouTube tutorial

import os
import sys
import socket

OK=0
ERROR=-1

def main():
    # Get the port to listen on from the command line arguments
    if len(sys.argv) < 2:
        print("Usage: server.py <port> where <port> is between 1024-49151 exclusive.")
        print("Done.")
        return ERROR

    print("[*] S: Creating new TCP endpoint...")

    # create a server socket
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    print("[*] S: Getting local machine IP address...")

    # Get the IP address of the server
    ip = socket.gethostbyname(socket.gethostname())

    # port (user-defined)
    port = 9000

    print("[*] S: Configured to listen on port", port)

    address = (ip,port)

    print("[*] S: Binding TCP endpoint to", ip, " on port", port, "...")

    server.bind(address)

    server.listen(128)

    print("[*] S: Started listening on IP address", ip, "and port", port, "...")

    client, addr = server.accept()

    print("[*] S: Got a connection from IP address", addr[0], "on port", addr[1])

    while True:
        try:
            data = client.recv(1024)
            print("[*] C:", data.decode())
            if(data==b'QUIT'):
                client.send("Goodbye!")
                print("[*] S: Goodbye!")
                print("[*] S: <disconnected>")
                client.close()
                break
            elif len(data)>0:
                # Echo the data back
                print("[*] S:", data)
                client.send(data)
        except:
            break
        
    print("[*] S: Closing endpoint...")

    server.close()

    print("[*] S: done.")
    return OK

if __name__ == "__main__":
    main()