import socket

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Timeout of 3 seconds
client.settimeout(3)

client.connect((HOST, PORT))

filename = "sample.txt"

# r means read and b meas binary mode.
with open(filename, "rb") as file: 

    while True:

        chunk = file.read(100)

        if not chunk:
            break

        while True:
            try:
                client.sendall(chunk)
                # 1024 means maximum nuber of byte that can receive
                ack = client.recv(1024)

                # b means byte data
                if ack == b"ACK":
                    print("Chunk sent successfully.")
                    break

            except socket.timeout:
                print("Timeout! Retransmitting chunk...")

client.sendall(b"EOF")

client.close()

print("File transfer completed.")