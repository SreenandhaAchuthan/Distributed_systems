import socket
SERVER_IP = "11.12.2.108"
CLIENT_IP = "11.12.19.41"
PORT = 6000
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#Bind client to its own IP address
client.bind((CLIENT_IP, 0))
#Connect to PC1 server
client.connect((SERVER_IP, PORT))
print("PC2: Connected to DSM Server")
print("Client IP:", CLIENT_IP)
print("Server IP:", SERVER_IP)
#Receive shared variable
data = client.recv(1024)
shared_value = int(data.decode())
print("Value received from PC1:", shared_value)
#Take user input
new_value = int(input("Enter the new shared value: "))
#Update shared variable
shared_value = new_value
print("Updated value:", shared_value)
#Send updated value to PC1
client.sendall(str(shared_value).encode())
print("Updated value sent to PC1")
client.close()