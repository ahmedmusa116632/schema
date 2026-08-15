import socket

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

try:

    while True:

        # Send first
        message = input("You: ")

        client.sendall(message.encode())

        # Wait for reply
        reply = client.recv(1024).decode()

        print("Server:", reply)

except KeyboardInterrupt:
    print("\nChat closed.")

client.close()