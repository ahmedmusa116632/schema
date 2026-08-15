import socket

# Create a UDP socket
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

message = "Hello"

# Send the message to localhost on port 5000
client.sendto(message.encode(), ("127.0.0.1", 5000))

print("Message sent!")

client.close()