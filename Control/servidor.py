from threading import Thread
import socket

class Servidor:
    """
    A class que representa o servidor do sistema.

    ...

    Atributos
    ----------
    Host: str
        ip utilizado
    Port: int
        numero de porta
    sock: socket
        soquete do servidor
    lixeiras: list
        lixeiras no sistema 
    lixeirasColetar: list
        lixeiras para serem coletadas
    adm: Administrador
        administradores conectados ao servidor
    caminhoes: Caminhao
        caminhoes conectados ao servidor
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
        self.__socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.__clientes = []
        """self.__lixeiras = []
        self.__lixeirasColetar = []
        self.__adms = []
        self.__caminhoes = []"""

        #inicia o servidor
        self.iniciar()

    def iniciar(self):
        """
        Metodo que permite multiplos clientes se conectarem ao servidor por meio de threads
        """
        try:
            #o metodo bind associa o socket servidor a um endereço 
            self.__socketServer.bind((self.__Host, self.__Port)) 
            #o metodo listen começa a escutar os pedidos de conexao, recebe como parametro o limite de conexoes
            self.__socketServer.listen()

            print("Aguardando conexões...")

            while True:
                #o metodo accept aceita a conexao de um cliente e retorna sua conexao e o endereco
                conexao, endereco = self.__socketServer.accept()

                thread = Thread(target=self.mensagensRecebidas, args=(conexao, endereco,))
                thread.start()
               
                self.__clientes.append(conexao)
                #adiciona a conexao numa lista de mensagensRecebidas ativas

        except Exception as ex:
            print(f"Erro ao inicar servidor. {ex.args[1]}")

    def mensagensRecebidas(self, conexao, endereco):
        """
        Gerencia as conexoes com o servidor
        """
        #Troca de mensagens
        while True:
            print("msg")
            try:
                #o metodo aguarda um dado enviado pela rede de até 1024 Bytes
                msg = conexao.recv(1024).decode()
                
                #quando os dados forem recebidos
                if not msg:
                    print('Fechando conexão...')
                    conexao.close()
                    break
                
            except Exception as ex:
                print(f"Erro ao receber mensagens ({ex})")


    def deletarCliente(self):
        """
        Elimina o cliente especificado na lista
        """
        pass

s = Servidor()