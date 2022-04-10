from threading import Thread
#from Api import Api
import json, select, queue, socket

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

    def __init__(self, Host = "127.0.0.1", Port = 50000):
        """
        Metodo construtor
            @param - Host : str
                ip utilizado
            @param - Port : int
                numero de porta
        """
        self.__Host = Host
        self.__Port = Port
        self.__socketServerList = []
        self.__lixeiras = {}
        self.__adms = {}
        self.__caminhoes = {}

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
            print(f"Aguardando conexões para porta {8080+i}")
            
            Thread(target=self.conecta, args=(socketServer,)).start()
            self.__socketServerList.append(socketServer) #adiciona os soquetes na lista de soquetes de servidor

    def conecta(self, socketServer: socket.socket):
        """
        Metodo que permite multiplos clientes se conectarem ao servidor por meio de threads
        """
        #try:
        """while True:
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
            
            print(f"cliente conectado! Porta: {socketServer.getsockname()[1]}")
            self.mensagensRecebidas(conexao)"""
        inputs = [socketServer]
        outputs = []
        message_queues = {}

        while inputs:
            readable, writable, exceptional = select.select(inputs, outputs, inputs)
            
            for s in readable:
                if s is socketServer:
                    connection, client_address = s.accept()
                    inputs.append(connection)
                    message_queues[connection] = queue.Queue()
                else:
                    data = s.recv(1024).decode()
                    if data:
                        message_queues[s].put(data)
                        data = json.loads(data)
                        print('Dado no Servidor: ',data['id'], client_address[1])
                        
                        #adiciona a conexao numa lista de referente ao tipo de objeto
                        if(socketServer.getsockname()[1] == 8080):
                            if client_address[1] not in self.__lixeiras: 
                                self.__lixeiras[data['id']] = connection

                            print("Lixeiras: ", self.__lixeiras)
                        elif(socketServer.getsockname()[1] == 8081):
                            if client_address[1] not in self.__caminhoes: 
                                self.__caminhoes[data['id']] = connection
            
                            print("Caminhões: ", self.__caminhoes)
                        else:
                            if client_address[1] not in self.__caminhoes: 
                                self.__adms[data['id']] = connection

                                #enviando todas as lixeiras para o adm
                                print(" ", type(self.__lixeiras))
                                ##msg = json.dumps(self.__lixeiras).encode("utf-8")
                                #connection.sendall(msg)
                        
                            print("Administradores: ", self.__adms)
                        if s not in outputs:
                            outputs.append(s)
                    else:
                        if s in outputs:
                            outputs.remove(s)
                        inputs.remove(s)
                        s.close()
                        del message_queues[s]

            """for s in writable:
                try:
                    print('----------', s)
                    next_msg = message_queues[s].get_nowait()
                except queue.Empty:
                    outputs.remove(s)
                else:
                    # if apiResponse != None: socketServer.sendto(json.dumps(apiResponse).encode("utf-8"), client_address)
                    s.send(next_msg)

            for s in exceptional:
                inputs.remove(s)
                if s in outputs:
                    outputs.remove(s)
                s.close()
                del message_queues[s]"""

        """except Exception as ex:
            print("Erro no servidor => ", ex)"""

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
                    print(msg)
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