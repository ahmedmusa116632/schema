import socket
import threading

HOST = "127.0.0.1"
PORT = 5000


def receive_messages(client):
    while True:
        try:
            data = client.recv(1024)

            if not data:
                print("\nServer disconnected.")
                break

            print(f"\nServer: {data.decode()}")

        except:
            break

    client.close()


# Create TCP socket
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect
client.connect((HOST, PORT))

print("Connected to server.")

# Start receiver thread
threading.Thread(target=receive_messages, args=(client,), daemon=True).start()

# Main thread sends messages
while True:
    try:
        message = input("Client: ")

        if message.lower() == "exit":
            break

        client.sendall(message.encode())

    except:
        break

client.close()