import socket
import threading

HOST = "127.0.0.1"
PORT = 5000

TOTAL_CLIENTS = 5

votes = []
clients = []

lock = threading.Lock()


def handle_client(client):

    vote = client.recv(1024).decode().upper()

    with lock:
        votes.append(vote)

    print("Vote received:", vote)


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((HOST, PORT))

server.listen()

print("Waiting for 5 clients...\n")

threads = []

while len(clients) < TOTAL_CLIENTS:

    client, address = server.accept()

    print("Connected:", address)

    clients.append(client)

    t = threading.Thread(target=handle_client, args=(client,))
    t.start()

    threads.append(t)


for t in threads:
    t.join()


countA = votes.count("A")
countB = votes.count("B")

if countA > countB:
    result = f"""
Election Result

Candidate A : {countA}
Candidate B : {countB}

Winner : Candidate A
"""

elif countB > countA:
    result = f"""
Election Result

Candidate A : {countA}
Candidate B : {countB}

Winner : Candidate B
"""

else:
    result = f"""
Election Result

Candidate A : {countA}
Candidate B : {countB}

Election Draw
"""


print(result)

for client in clients:

    client.sendall(result.encode())

    client.close()

server.close()