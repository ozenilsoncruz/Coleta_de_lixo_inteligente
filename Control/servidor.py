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

    def __init__(self):
        """
        Metodo construtor
            @param - Host : str
                ip utilizado
            @param - Port : int
                numero de porta
        """
        self.__socketServerList = []
        self.__lixeiras = []
        self.__lixeirasColetar = []
        self.__adms = []
        self.__caminhoes = []

        #inicia o servidor
        self.iniciar()
 
    def iniciar(self):
        """ 
        Inicia o servidor com 3 sockets com portas diferentes
        """
        for i in range(0, 3):
            socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
            socketServer.bind(("127.0.0.1", 8080+i)) #o metodo bind associa o socket servidor a um endereço
            socketServer.listen() #o metodo listen começa a escutar os pedidos de conexao, recebe como parametro o limite de conexoes

            Thread(target=self.conecta, args=(socketServer,)).start()
            self.__socketServerList.append(socketServer) #adiciona os soquetes na lista de soquetes de servidor

            print(f"Aguardando conexões para porta {8080+i}")

    def conecta(self, socketServer):
        """
        Metodo que permite multiplos clientes se conectarem ao servidor por meio de threads
        """
        try:
            while True:
                #o metodo accept aceita a conexao de um cliente e retorna sua conexao e o endereco
                conexao, endereco = socketServer.accept()
                                                    #Thread(target=self.mensagensRecebidas, args=(conexao, endereco,)).start()
                #adiciona a conexao numa lista de referente ao tipo de objeto
                if(socketServer.getsockname()[1] == 8080):
                    self.__lixeiras.append(conexao)
                elif(socketServer.getsockname()[1] == 8081):
                    self.__caminhoes.append(conexao)
                else:
                    self.__adms.append(conexao)
        except Exception as ex:
            print(f"Erro ao inicar servidor. {ex.args[1]}")

    def mensagensRecebidas(self, conexao):
        """
        Gerencia as conexoes com o servidor
        """
        try:
            while True:
                #o metodo aguarda um dado enviado pela rede de até 1024 Bytes
                msg = conexao.recv(1024).decode()
                #quando os dados forem recebidos
                if not msg:
                    print('Fechando conexão...')
                    break
        except Exception as ex:
            print(f"Erro ao receber mensagens ({ex})")
        finally: 
            conexao.close()

    def deletarCliente(self):
        """
        Elimina o cliente especificado na lista
        """
        pass

s = Servidor()

