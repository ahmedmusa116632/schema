import socket

HOST = "127.0.0.1"
PORT = 5000

server = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

server.bind((HOST, PORT))

print("UDP Chat Server Running...")

client_address = None

try:

    while True:

        message, client_address = server.recvfrom(1000)

        print("\nClient:", message.decode())

        reply = input("You: ")

        reply = reply[:1000]      # Maximum 1000 characters

        server.sendto(reply.encode(), client_address)

except KeyboardInterrupt:

    print("\nChat closed.")

server.close()