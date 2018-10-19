# This code was typed out referencing a YouTube tutorial

import socket

# create a server socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Get the IP address of the server
ip = socket.gethostbyname(socket.gethostname())

# port (user-defined)
port = 9000

address = (ip,port)

server.bind(address)

server.listen(128)

print("[*] Started listening on ", ip, "and", port)

client, addr = server.accept()

print("[*] Got a connection from ", addr[0], "on port", addr[1])

while True:
    data = client.recv(1024)
    print("[*] C:", data)

    print("[*] Processing the data...")
    if (data=="Hello server"):
        client.send("Hello client")
        print("[*] S: Hello client")
    elif(data=="QUIT"):
        client.send("Goodbye!")
        print("[*] S: Goodbye!")
        print("[*] S: <disconnected>")
        client.close()
        break
    else:
        # Echo the data back
        print("[*] S:", data)
        client.send(data)

server.close()
print("[*] Server: done.")
