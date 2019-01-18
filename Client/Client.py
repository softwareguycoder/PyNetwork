import socket
import sys
import time

OK=0
ERROR=-1
NUMARGS=3

def create_endpoint():
    client = socket.socket()
    return client

def main():
    if len(sys.argv) != NUMARGS:
        print("Usage: client <serverIP> <port>")
        input()
        return ERROR

    try:
        client = create_endpoint()

        try:
            server=sys.argv[1]
            port=int(sys.argv[2])

            print("[*] C: Waiting for the server to initialize...")

            time.sleep(3)

            print("[*] C: Attempting to connect to the server", server, " on port", port, "...")

            client.connect((server, port))

            print("[*] C: Connected to the server", server, " on port", port, ".")
            print()
            print("Type the text you want to send to the server at the prompt.")

            while True:
                text=input("> ")
                if text=='':
                    continue
                client.sendall(text.encode())
                if text.upper()=='QUIT':
                    print("[*] S: <disconnected>")
                    break
                received=client.recv(len(text))
                print("[*] S:", received.decode())
        except:
            print("A problem occurred while communicating with the server.")
            return ERROR
        finally:
            client.close()

    except:
        print("A problem occurred while communicating with the server.")
        return ERROR

    return OK

if __name__ == "__main__":
    main()