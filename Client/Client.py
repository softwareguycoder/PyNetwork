import socket

# Create a client socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# connect to a server
ip=socket.gethostbyname("www.google.com")

print("IP address of www.google.com is:", ip)

port=80

# Bind the IP address and the port into a tuple
address=(ip,port)

client.connect(address)

bytes = client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

print("{} bytes have been sent to www.google.com".format(bytes))

data = client.recv(1024)
print(data)
input()

