import socket

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

try:

    while True:

        message = input("You: ")

        message = message[:1000]

        client.sendto(message.encode(), (HOST, PORT))

        reply, _ = client.recvfrom(1000)

        print("Server:", reply.decode())

except KeyboardInterrupt:

    print("\nChat closed.")

client.close()