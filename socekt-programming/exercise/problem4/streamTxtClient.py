import socket

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

filename = input("Enter text file name: ")

client.sendto(filename.encode(), (HOST, PORT))

save_name = "received_" + filename

total = 0
preview_shown = False

with open(save_name, "wb") as file:

    while True:

        data, _ = client.recvfrom(2048)

        if data == b"ERROR":
            print("File not found.")
            break

        if data == b"EOF":
            print("\nStreaming Finished")
            break

        file.write(data)

        total += len(data)

        print(f"Received {len(data)} bytes (Total = {total})")

        # After enough data has arrived, show the beginning of the file
        if total >= 5000 and not preview_shown:

            preview_shown = True

            file.flush()

            print("\n------ Preview of received text ------\n")

            with open(save_name, "r", encoding="utf-8", errors="ignore") as f:
                print(f.read(300))

            print("\n--------------------------------------")
            print("Downloading is still in progress...\n")

client.close()