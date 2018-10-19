# This code was typed out referencing a YouTube tutorial

import socket

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

print("[*] S: Started listening on ", ip, "and", port, "...")

client, addr = server.accept()

print("[*] S: Got a connection from ", addr[0], "on port", addr[1])

while True:
    data = client.recv(1024)
    print("[*] C:", data)

    print("[*] S: Processing the data...")
    if(data=="QUIT"):
        client.send("Goodbye!")
        print("[*] S: Goodbye!")
        print("[*] S: <disconnected>")
        client.close()
        break
    else:
        # Echo the data back
        print("[*] S:", data)
        client.send(data)

print("[*] S: Closing endpoint...")

server.close()

print("[*] S: done.")
