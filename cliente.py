import socket

class Cliente:

    #Metodo construtor
    def __init__(self):
        self._Host = '127.0.0.1' #ip utilizado
        self._Port = 50000 #numero de porta
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    """
    Conecta a lixeia ao servidor
    """
    def conectar(self):
        self._sock.connect((self._Host, self._Port))

    """
    Recebe dados através do servidor
    """
    def receberDados(self):
        print(self._sock.recv(1024))
        return self._sock.recv(1024)

    """
    Envia dados para o servidor
    """
    def enviarDados(self, msg):
        self._sock.sendall(str.encode(msg))