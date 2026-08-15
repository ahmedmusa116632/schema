import socket
import threading

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

sock.bind(("0.0.0.0", 5001))

TARGET_IP = "127.0.0.1"
TARGET_PORT = 5000


def receive():
    while True:
        data, addr = sock.recvfrom(1024)
        print(f"\nFriend: {data.decode()}")


threading.Thread(target=receive, daemon=True).start()

print("Simple UDP Chat")
print("Type messages and press Enter.\n")

while True:
    message = input("You: ")
    sock.sendto(message.encode(), (TARGET_IP, TARGET_PORT))