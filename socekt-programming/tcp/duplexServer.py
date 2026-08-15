import socket
import threading

HOST = "127.0.0.1"
PORT = 5000


def receive_messages(conn):
    while True:
        try:
            data = conn.recv(1024)

            if not data:
                print("\nClient disconnected.")
                break

            print(f"\nClient: {data.decode()}")

        except:
            break

    conn.close()


# Create TCP socket
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind
server.bind((HOST, PORT))

# Listen
server.listen(1)

print(f"Server listening on {HOST}:{PORT}")

# Accept client
conn, addr = server.accept()

print(f"Connected by {addr}")

# Start receiver thread
threading.Thread(target=receive_messages, args=(conn,), daemon=True).start()

# Main thread sends messages
while True:
    try:
        message = input("Server: ")

        if message.lower() == "exit":
            break

        conn.sendall(message.encode())

    except:
        break

conn.close()
server.close()