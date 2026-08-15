import socket

# Create a UDP socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind the socket to localhost on port 5000
server.bind(("127.0.0.1", 5000))

print("Receiver is waiting for a message...")

# Wait for one message
data, address = server.recvfrom(1024)

print("Received:", data.decode())
print("Sent by:", address)

server.close()