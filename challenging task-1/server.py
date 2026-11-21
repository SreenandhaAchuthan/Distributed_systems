import socket
SERVER_IP = "11.12.19.41"
PORT = 6000
shared_value = 3
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server.bind((SERVER_IP, PORT))
server.listen(1)
print("PC1: DSM Server started...")
print("Server IP:", SERVER_IP)
print("Waiting for PC2...")
conn, addr = server.accept()
print("Connected to Client:", addr)
print("Initial shared value:", shared_value)
conn.sendall(str(shared_value).encode())
data = conn.recv(1024)
if data:
    shared_value = int(data.decode())
print("Updated shared value:", shared_value)
conn.close()
server.close()