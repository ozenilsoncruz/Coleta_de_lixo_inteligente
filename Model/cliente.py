import socket

class Cliente:
    """
    A class que representa o cliente que se conecta ao servidor.

    ...

    Atributos
    ----------
    Host : str
        ip utilizado
    Port : int
        numero de porta
    sock : socket
        soquete

    Metodos
    -------
    conectar():
        Conecta a lixeia ao servidor.

    receberDados():
        Recebe dados através do servidor

    enviarDados(msg):
        Envia dados para o servidor
    """

    def __init__(self, Host = '127.0.0.1', Port = 50000):
        """
        Metodo construtor
            @param Host : str
                    ip utilizado
            @param Port : int
                    numero de porta
        """

        self._Host = Host #ip utilizado
        self._Port =  Port #numero de porta
        self._sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def conectar(self):
        """
        Conecta a lixeia ao servidor
        """
        try:    
            self._sock.connect((self._Host, self._Port)) 
        except ConnectionRefusedError:
            print("Conexão recusada")
        except:
            print("Erro desconhecido")
            
    def receberDados(self):
        """
        Recebe dados através do servidor
        """
        print(self._sock.recv(1024))
        return self._sock.recv(1024)

    def enviarDados(self, msg):
        """
        Envia dados para o servidor
            @param msg: str
                mensagem que sera enviada para o servidor
        """
        self._sock.sendall(str.encode(msg))