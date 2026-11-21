import socket
import os
import json

SERVER_IP = "11.12.2.108"
PORT = 6001

SHARED_FOLDER = r"C:\SharedFiles"

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((SERVER_IP, PORT))
server.listen(5)

print("Peer Server Started...")
print("Shared Folder:", SHARED_FOLDER)
print("Waiting for client requests...")

while True:

    conn, addr = server.accept()

    print("Connected to:", addr)

    if os.path.isdir(SHARED_FOLDER):

        files = sorted(
            name for name in os.listdir(SHARED_FOLDER)
            if os.path.isfile(os.path.join(SHARED_FOLDER, name))
        )

        response = json.dumps(files)

    else:

        response = json.dumps(
            {"error": "Shared folder not found"}
        )

    conn.sendall(response.encode("utf-8"))

    print("File list sent successfully.")

    conn.close()