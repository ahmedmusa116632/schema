import socket

HOST = "127.0.0.1"
PORT = 5000

# Create TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket
server.bind((HOST, PORT))

# Listen for incoming connections
server.listen()

print(f"Receiver listening on {HOST}:{PORT}")

# Accept a sender
client_socket, addr = server.accept()

print("Connected by:", addr)

# Receive messages continuously
while True:
    data = client_socket.recv(1024)

    if not data:
        break

    print("Received:", data.decode())

client_socket.close()
server.close()