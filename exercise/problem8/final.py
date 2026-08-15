import socket
import struct
import threading

GROUP = "224.1.1.1"
PORT = 5000
TOTAL_VOTERS = 5

votes = []

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
sock.bind(("", PORT))

mreq = struct.pack("4sL", socket.inet_aton(GROUP), socket.INADDR_ANY)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_ADD_MEMBERSHIP, mreq)
sock.setsockopt(socket.IPPROTO_IP, socket.IP_MULTICAST_LOOP, 1)


def receive_votes():

    while len(votes) < TOTAL_VOTERS:

        data, _ = sock.recvfrom(1024)
        vote = data.decode().upper()

        if vote in ["A", "B"]:
            votes.append(vote)
            print("Vote received:", vote)

    countA = votes.count("A")
    countB = votes.count("B")

    print("\n--- Election Result ---")
    print("Candidate A:", countA)
    print("Candidate B:", countB)

    if countA > countB:
        print("Winner: Candidate A")
    elif countB > countA:
        print("Winner: Candidate B")
    else:
        print("Result: Tie")


thread = threading.Thread(target=receive_votes)
thread.start()

print("Start this program in all 5 terminals first.")
input("Then press ENTER in each terminal...")


while True:

    vote = input("Vote (A/B): ").upper()

    if vote in ["A", "B"]:
        break

    print("Invalid vote.")


sock.sendto(vote.encode(), (GROUP, PORT))

print("Vote cast successfully.")

thread.join()

sock.close()