import socket

HOST = "127.0.0.1"
PORT = 5000

# Create TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind server
server.bind((HOST, PORT))

# Listen for clients
server.listen()

print("Calculator Server is running...")

while True:
    client_socket, client_address = server.accept()

    print(f"\nConnected with {client_address}")

    # Receive data
    data = client_socket.recv(1024).decode()

    # Expected format: number1,number2,operator
    num1, num2, operator = data.split(",")

    num1 = int(num1)
    num2 = int(num2)

    # Perform calculation
    if operator == "+":
        result = num1 + num2

    elif operator == "-":
        result = num1 - num2

    elif operator == "*":
        result = num1 * num2

    elif operator == "/":
        if num2 == 0:
            result = "Error: Division by zero"
        else:
            result = num1 / num2

    elif operator == "%":
        if num2 == 0:
            result = "Error: Modulo by zero"
        else:
            result = num1 % num2

    else:
        result = "Invalid Operator"

    # Send result back
    client_socket.sendall(str(result).encode())

    client_socket.close()