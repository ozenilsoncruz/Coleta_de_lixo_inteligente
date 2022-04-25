import json, select, socket, Api

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
    lixeiras: dict()
        dicionario com as lixeiras no sistema 
    lixeirasColetar: list()
        lista das lixeiras para serem coletadas
    adm: dict()
        dicionario com administradores conectados ao servidor
    caminhoes: dict()
        dicionario com os caminhoes conectados ao servidor
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
        self.conecta()

    def conecta(self):
        # """
        # Metodo que permite multiplos clientes se conectarem ao servidor por meio de threads
        # """
        # try:
            #inicia o servidor
            socketServer = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  
            socketServer.bind((self.__Host, self.__Port)) #o metodo bind associa o socket servidor a um endereço
            socketServer.listen() #o metodo listen começa a escutar os pedidos de conexao, recebe como parametro o limite de conexoes
            print(f"Aguardando conexões...")

            entradas = [socketServer]
            saidas = []

            while entradas:
                leitura, _, _ = select.select(entradas, saidas, entradas)
                for s in leitura:
                    #se s for o socket de servidor, ele aceitara as conexoes e adicona essa conexao na lista de entradas
                    if s is socketServer:
                        conexao, endereco = s.accept()
                        entradas.append(conexao)

                    #senao, verifica a mensagem recebida pela conexao do cliente
                    else:
                       # try:
                            mensagem = s.recv(2048).decode()
                            if(mensagem):
                                mensagem = json.loads(mensagem)
                                #adiciona a conexao numa lista de referente ao tipo de objeto
                                if(mensagem['tipo'] == 'lixeira'):
                                    Api.mensagemLixeira(conexao, mensagem)
                                elif(mensagem['tipo'] == 'caminhao'):
                                    Api.mensagemCaminhao(conexao, mensagem)
                                elif(mensagem['tipo'] == 'adm'):
                                    Api.mensagemAdm(conexao, mensagem)
                                else:
                                    print(mensagem)
                                if s not in saidas:
                                    saidas.append(s)
        #                 except:
        #                     #remove o cliente do sistema
        #                     print(Api.deletarCliente(s))
        #                     #remove o cliente da lista de interacoes no select
        #                     if s in saidas:
        #                         saidas.remove(s)
        #                     entradas.remove(s)
        # except Exception as ex:
        #   print("Problema no servidor => ", ex)

Servidor()