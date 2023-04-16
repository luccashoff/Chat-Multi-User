import socket

HOST = 'localhost'
PORT = 50000

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket.bind((HOST, PORT))
socket.listen()
print('Aguardando conexão de um Cliente')
connection, address = socket.accept()

print('Conectado em', address)
while True:
    data = connection.recv(1024)
    if not data:
        print('Fechando a Conexão.')
        connection.close()
        break
    connection.sendall(data)
