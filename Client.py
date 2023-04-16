import socket

HOST = 'localhost'
PORT = 50000

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.connect((HOST, PORT))
socket.sendall(str.encode('Bom dia Grupo!'))
data = socket.recv(1024)

print('Mensagem Ecoada:', data.decode())