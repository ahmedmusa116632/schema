import socket

host = "127.0.0.1"
port = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind(host, port)
server.listen(1)

print("waiting for client")

conn, addr = server.accpet()
print("connected by", addr)

outfile = open()