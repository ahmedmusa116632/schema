import socket

HOST = "127.0.0.1"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
# 1 means the maximum number of queued connections.
server.listen(1)

print("Waiting for client...")

conn, addr = server.accept()
print("Connected by", addr)

outfile = open("received_tcp.txt", "wb")

while True:
    data = conn.recv(100)

    if data == b"EOF":
        print("File received successfully.")
        break

    outfile.write(data)

    # Send acknowledgment
    conn.sendall(b"ACK")

outfile.close()
conn.close()
server.close()