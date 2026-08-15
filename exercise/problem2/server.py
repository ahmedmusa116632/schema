import socket
import threading
import time
import os

HOST = "127.0.0.1"
PORT = 5000


def send_file(client_socket, filename):
    print(f"Thread started for {filename}")

    # Check whether the file exists
    if not os.path.exists(filename):
        client_socket.sendall(b"File not found")
        client_socket.close()
        return

    # Open the requested file
    with open(filename, "rb") as file:

        while True:
            data = file.read(1000)  # Read at most 1000 bytes

            if not data:
                break

            client_socket.sendall(data)  # Send data
            print(f"Sent {len(data)} bytes from {filename}")

            time.sleep(0.2)  # Wait 200 milliseconds

    print(f"{filename} transfer complete")

    client_socket.close()


# Create TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))

server.listen()

print("Server is running...")

while True:

    client_socket, client_address = server.accept()

    print(f"\nConnected with {client_address}")

    filename = client_socket.recv(1024).decode()

    print("Requested:", filename)

    thread = threading.Thread(
        target=send_file,
        args=(client_socket, filename)
    )

    thread.start()