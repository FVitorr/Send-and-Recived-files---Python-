import socket

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

rHost = '127.0.0.1'
rPort = 7777

client.connect ((rHost,rPort))
print ('Conectado...')

namefile = str(input('arq>'))

client.send(namefile.encode())

with open (namefile,'wb') as file:
    while True:
        data = client.recv(100000)
        if not data:
            break
        file.write(data)
print(f'{namefile} recebido')        
