import socket

HOST = "127.0.0.1"
PORT = 5000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))

filename = input("Enter file name (file1.txt/file2.txt/file3.txt): ")

client.sendall(filename.encode())

save_name = "downloaded_" + filename

with open(save_name, "wb") as file:

    while True:

        data = client.recv(1000)

        if not data:
            break

        file.write(data)

print("Download complete.")
print("Saved as:", save_name)

client.close()