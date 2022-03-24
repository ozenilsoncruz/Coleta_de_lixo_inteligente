import socket

Host = '127.0.0.1' #ip utilizado
Port = 50000 #numero de porta

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#Conecta o cliente ao servidor
sock.connect((Host, Port))

#envia os dados para o servidor
sock.sendall(str.encode('Hello World!!'))

#recebe os dados enviados pelo servidor
dados = sock.recv(1024)

print('Mensagem: ', dados.decode())