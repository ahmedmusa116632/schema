import socket

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

while True:

    vote = input("Cast Vote (A/B): ").upper()

    if vote in ("A", "B"):
        break

    print("Invalid vote.")

client.sendall(vote.encode())

result = client.recv(1024).decode()

print("\n")
print(result)

client.close()