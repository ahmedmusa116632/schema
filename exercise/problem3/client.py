import socket

HOST = "127.0.0.1"
PORT = 5000

# Create TCP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to server
client.connect((HOST, PORT))

# Input from user
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /, %): ")

# Send data
message = f"{num1},{num2},{operator}"

client.sendall(message.encode())

# Receive result
result = client.recv(1024).decode()

print("Result =", result)

client.close()