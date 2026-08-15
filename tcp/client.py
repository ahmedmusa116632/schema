import socket

HOST = "127.0.0.1"
PORT = 5000

# Create TCP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the receiver
client.connect((HOST, PORT))

print("Connected to receiver.")

# Send messages continuously
while True:
    message = input("Enter message: ")

    if message.lower() == "exit":
        break

    client.sendall(message.encode())

client.close()