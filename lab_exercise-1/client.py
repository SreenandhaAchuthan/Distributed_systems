import socket

SERVER_IP = "11.12.2.108"  # PC1 IP address
PORT = 6000

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((SERVER_IP, PORT))

print("Connected to the server.")

while True:
    message = input("Client message: ")

    client.sendall(message.encode())

    if message.lower() == "exit":
        break

    reply = client.recv(1024).decode()

    print("Server:", reply)

    if reply.lower() == "exit":
        break

client.close()

print("Client disconnected.")