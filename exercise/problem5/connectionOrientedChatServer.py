import socket

HOST = "127.0.0.1"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))
server.listen(1)

print("Waiting for client...")

client_socket, address = server.accept()

print("Connected with", address)

try:
    while True:

        # Receive first
        message = client_socket.recv(1024).decode()

        if not message:
            break

        print("\nClient:", message)

        # Send reply
        reply = input("You: ")

        client_socket.sendall(reply.encode())

except KeyboardInterrupt:
    print("\nChat closed.")

client_socket.close()
server.close()