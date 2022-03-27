
from threading import Thread
import socket

class Servidor:
    """
    A class que representa o servidor do sistema.

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
            @param - Host : str
                ip utilizado
            @param - Port : int
                numero de porta
        """
        self.__Host = Host #ip utilizado
        self.__Port = Port #numero de porta
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

        #o metodo bind associa o socket servidor a um endereço 
        self.__sock.bind((self.__Host, self.__Port)) 

    def permitirConexao(self):
        """
        Metodo que permite multiplos clientes se conectarem ao servidor por meio de threads
        """
        #o metodo listen começa a escutar os pedidos de conexao, recebe como parametro o limite de conexoes
        self.__sock.listen()
        print("Aguardando conexões...")

        while True:
             #o metodo accept aceita a conexao de um cliente e retorna a conexao e o endereco
            conexao, endereco = self.__sock.accept()

            thread = Thread(target=self.conexoes, args=(conexao, endereco,))
            thread.start()

    def conexoes(self, conexao, endereco):
        """
        Gerencia as conexoes com o servidor
        """
        print('Conectado em ', endereco)

        #Troca de mensagens
        while True:
            #o metodo aguarda um dado enviado pela rede de até 1024 Bytes
            msg = conexao.recv(1024)

            #quando os dados forem recebidos
            if not msg:
                print('Fechando conexão...')
                conexao.close()
                break
            
            #envia os dados de volta para o cliente
            conexao.sendall(msg)
    
    def encerrarConexao(self, conexao):
        conexao.close()

s = Servidor()
s.permitirConexao()
