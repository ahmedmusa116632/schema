import socket

HOST = "127.0.0.1"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind((HOST, PORT))

outfile = open("received_udp.txt", "w", encoding="utf-8")

print("UDP Server Listening...")

while True:

    data, addr = server.recvfrom(1024)

    text = data.decode()

    if text == "EOF":
        print("File received.")
        break

    outfile.write(text)

outfile.close()
server.close()