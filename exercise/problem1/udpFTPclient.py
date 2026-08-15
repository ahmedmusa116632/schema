import socket

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

filename = "sample.txt"

with open(filename, "r", encoding="utf-8") as file:

    for line in file:
        client.sendto(line.encode(), (HOST, PORT))
        print("Sent:", line.strip())

client.sendto(b"EOF", (HOST, PORT))

client.close()

print("Transfer complete.")