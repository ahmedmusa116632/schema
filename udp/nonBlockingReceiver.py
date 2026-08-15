import socket
import time

HOST = "127.0.0.1"
PORT = 5000

# Create UDP socket
server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to port
server.bind((HOST, PORT))

# Make socket non-blocking
server.setblocking(False)

print(f"Listening on {HOST}:{PORT}")

while True:
    try:
        data, addr = server.recvfrom(1024)
        print(f"\nReceived from {addr}: {data.decode()}")

    except BlockingIOError:
        # No packet available right now
        print("No message... Doing other work.")

    # Simulate other work
    time.sleep(1)