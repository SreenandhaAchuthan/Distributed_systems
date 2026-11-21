import socket
import json

SERVER_IP = "11.12.2.108"
PORT = 6001

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((SERVER_IP, PORT))

print("Connected to Peer Server.")

data = b""

while True:

    chunk = client.recv(4096)

    if not chunk:
        break

    data += chunk

client.close()

files = json.loads(data.decode("utf-8"))

print("\nFiles available in shared folder:")

if isinstance(files, dict):

    print(files["error"])

elif not files:

    print("No files available.")

else:

    for file in files:

        print(file)