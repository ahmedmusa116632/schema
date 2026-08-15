import socket
import threading

# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Bind to this computer's port
sock.bind(("0.0.0.0", 5000))

# Address of Computer B
TARGET_IP = "127.0.0.1"      # Change if using another computer
TARGET_PORT = 5001


def receive():
    while True:
        data, addr = sock.recvfrom(1024)
        print(f"\nFriend: {data.decode()}")


# Start receiving thread . deamon true means that the thread will exit when the main program exits
threading.Thread(target=receive, daemon=True).start()

print("Simple UDP Chat")
print("Type messages and press Enter.\n")

while True:
    message = input("You: ")
    sock.sendto(message.encode(), (TARGET_IP, TARGET_PORT))