import socket
import random
import time
import os

HOST = "127.0.0.1"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server.bind((HOST, PORT))

print("Streaming Text Server Running...")

while True:

    filename, client_address = server.recvfrom(1024)
    filename = filename.decode()

    print(f"\nClient requested: {filename}")

    if not os.path.exists(filename):
        server.sendto(b"ERROR", client_address)
        continue

    with open(filename, "rb") as file:

        while True:

            chunk_size = random.randint(1000, 2000)

            data = file.read(chunk_size)

            if not data:
                break

            server.sendto(data, client_address)

            print(f"Sent {len(data)} bytes")

            time.sleep(0.2)

    server.sendto(b"EOF", client_address)

    print("Streaming completed.")