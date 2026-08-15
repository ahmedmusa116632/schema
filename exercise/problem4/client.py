import socket

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

filename = input("Enter media filename: ")

client.sendto(filename.encode(), (HOST, PORT))

save_name = "received_" + filename

total = 0

with open(save_name, "wb") as file:

    while True:

        data, _ = client.recvfrom(2048)

        if data == b"ERROR":
            print("File not found.")
            break

        if data == b"EOF":
            print("Streaming Finished")
            break

        file.write(data)

        total += len(data)

        print(f"Received {len(data)} bytes (Total = {total})")

        if total > 5000:
            print("Enough data received.")
            print("You can open the partially downloaded media file now.")

client.close()