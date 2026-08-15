import socket
import threading

HOST = "127.0.0.1"
PORT = 5000


def chat_with_client(client_socket, client_address):

    print(f"\n{client_address} connected.")

    try:
        while True:

            # Receive message from this client
            message = client_socket.recv(1024).decode()

            if not message:
                break

            print(f"\nClient {client_address}: {message}")

            # Send reply
            reply = input(f"Reply to {client_address}: ")

            client_socket.sendall(reply.encode())

    except ConnectionResetError:
        print(f"{client_address} disconnected.")

    finally:
        client_socket.close()
        print(f"{client_address} connection closed.")


# Create TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))

server.listen()

print("Server is waiting for clients...")

while True:

    client_socket, client_address = server.accept()

    # Create a new thread for every client
    thread = threading.Thread(
        target=chat_with_client,
        args=(client_socket, client_address)
    )

    thread.start()