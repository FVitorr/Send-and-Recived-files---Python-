import socket

serve = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

rHost = '127.0.0.1'
rPort = 7777

serve.bind((rHost,rPort))
serve.listen(1)

connection, address = serve.accept()

namefile = connection.recv(1024 * 4)

with open(namefile, 'rb') as file:
    for data in file.reaflines():
        connection.send(data)
    print('Arquivo enviado')
