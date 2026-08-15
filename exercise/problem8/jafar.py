import socket
import struct
import threading

GROUP = "224.0.0.1"
port = 5000

votes_A = 0
votes_B = 0


def receive_votes():

    global votes_A, votes_B

    receiver = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    receiver.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    receiver.bind(("", port))

    membership = struct.pack(
        "4sl",
        socket.inet_aton(GROUP),
        socket.INADDR_ANY
    )

    receiver.setsockopt(
        socket.IPPROTO_IP,
        socket.IP_ADD_MEMBERSHIP,
        membership
    )

    for i in range(4):

        data, addr = receiver.recvfrom(100)

        vote = data.decode()

        print(f"Vote received from {addr} : {vote}")

        if vote == "A":
            votes_A += 1
        elif vote == "B":
            votes_B += 1

    receiver.close()


sender = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

thread = threading.Thread(target=receive_votes)

thread.start()


vote = input("Cast your vote (A/B): ").upper()

if vote == "A":
    votes_A += 1
elif vote == "B":
    votes_B += 1
else:
    print("Invalid Vote")
    exit()

sender.sendto(vote.encode(), (GROUP, port))

print("Vote Sent")

thread.join()

print("\nFinal Result")

print("Candidate A :", votes_A)

print("Candidate B :", votes_B)

if votes_A > votes_B:
    print("Winner : Candidate A")

elif votes_B > votes_A:
    print("Winner : Candidate B")

else:
    print("Result : Tie")