import socket, json

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
        self._socketClient = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #tenta conectar o cliente ao servidor
        self.conectar()
        #self.receberDados(self)

    def conectar(self):
        """
        Conecta a lixeia ao servidor
        """
        try:    
            self._socketClient.connect((self._Host, self._Port)) 
        except ConnectionRefusedError:
            print("Conexão recusada")
        except:
            print("Erro desconhecido")
            
    def receberDados(self):
        """
        Recebe dados através do servidor
        """
        return self._socketClient.recv(1024).decode()

    def enviarDados(self, msg):
        """
        Envia dados para o servidor
            @param msg: str
                mensagem que sera enviada para o servidor
        """
        try:
            print(msg, " ", type(msg))
            msg = json.dumps(msg).encode("utf-8")
            self._socketClient.sendall(msg)
        except Exception as ex:
            print("Não foi possivel enviar a mensagem => ", ex) 