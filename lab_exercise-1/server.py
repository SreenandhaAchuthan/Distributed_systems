import socket

SERVER_IP = "11.12.19.41"  # PC1 IP address
PORT = 6000

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server.bind((SERVER_IP, PORT))
server.listen(1)

print("Server is waiting for a client...")

conn, addr = server.accept()
print("Connected to:", addr)

while True:
    message = conn.recv(1024).decode()

    if not message:
        break

    print("Client:", message)

    if message.lower() == "exit":
        break

    reply = input("Server reply: ")
    conn.sendall(reply.encode())

    if reply.lower() == "exit":
        break

conn.close()
server.close()

print("Server closed.")