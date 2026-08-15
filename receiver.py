import time
import socket

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

client.bind(("127.0.0.1", 5000))

client.setblocking(False)

while True:
    try:
        data, address = client.recvfrom(1024)
        print(f"Received message: {data.decode()} from {address}")
    except BlockingIOError:
        print("No data received, waiting...")
    time.sleep(1)