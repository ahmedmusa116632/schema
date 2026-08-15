import socket
#struct use to format binary data
import struct
import threading

GROUP = "224.1.1.1"
PORT = 5000


# Create UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Allow multiple processes to use the same port
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

# Bind to the port
sock.bind(("", PORT))


# Join multicast group
group = socket.inet_aton(GROUP)

#mreq means multicas request, 4s measn 4-bute string. L means unsigned long integer
mreq = struct.pack("4sL", group, socket.INADDR_ANY)

sock.setsockopt(
    socket.IPPROTO_IP,
    socket.IP_ADD_MEMBERSHIP,
    mreq
)


# Function for receiving messages
def receive():

    while True:

        data, address = sock.recvfrom(1024)

        print("\nReceived:", data.decode())


# Create receiver thread
thread = threading.Thread(target=receive)

thread.daemon = True

thread.start()


# Main thread sends messages
while True:

    message = input("You: ")

    sock.sendto(
        message.encode(),
        (GROUP, PORT)
    )
