from threading import Thread
#from Api import Api
import json, select, socket

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
        self.__lixeiras = {}
        self.__lixeirasColetar = {}
        self.__adms = {}
        self.__caminhoes = {}

        self.conecta()

    def conecta(self):
        """
        Metodo que permite multiplos clientes se conectarem ao servidor por meio de threads
        """
        try:
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
                        mensagem = s.recv(1024).decode()
                        if(mensagem):
                            mensagem = json.loads(mensagem)
                            print("Conectado com: ", mensagem['tipo'], mensagem['id'])
                    
                            #adiciona a conexao numa lista de referente ao tipo de objeto
                            if(mensagem['tipo'] == 'lixeira'):
                                self.mensagemLixeira(conexao, mensagem)       

                            elif(mensagem['tipo'] == 'caminhao'):
                                self.mensagemCaminhao(conexao, mensagem)

                            elif(mensagem['tipo'] == 'adm'):
                                self.mensagemAdm(conexao, mensagem)

                            if s not in saidas:
                                saidas.append(s)
                        else:
                            if s in saidas:
                                saidas.remove(s)
                            entradas.remove(s)
                            #remover conexao da dicionario tb
                            #s.close()

        except Exception as ex:
            print("Erro no servidor => ", ex)

    def mensagemAdm(self, conexao, mensagem):
        """
        Gerencia as mensagens para o Adm
        """
        if mensagem['id'] not in self.__adms: 
            self.__adms[mensagem['id']] = conexao
            msg = json.dumps(str(self.__lixeiras)).encode("utf-8")
            conexao.sendall(msg)
        
        if(mensagem['acao'] != ''):
            msg = json.dumps({'acao': mensagem['acao'], 'idLixeira': mensagem['idLixeira'], 'idCaminhao': mensagem['idCaminhao']}).encode("utf-8")

            if self.__lixeiras.keys():
                #se a acao e o id da lixeira nao estiverem vazios
                if(mensagem['idLixeira'] !='' and mensagem['idCaminhao'] ==''):
                    if (self.__lixeiras[mensagem['idLixeira']]): 
                        self.__lixeiras[mensagem['idLixeira']][1].sendall(msg)
            if self.__lixeiras.keys() and self.__caminhoes.keys():
                #se a acao e o id da caminhao nao estiverem vazios
                if(mensagem['idCaminhao'] !='' and mensagem['idLixeira'] !=''):
                    if(self.__caminhoes[mensagem['idCaminhao']] and self.__lixeiras[mensagem['idLixeira']]):
                        self.__caminhoes[mensagem['idCaminhao']].sendall(msg)
                    else:
                        print("Não foi possível esvaziar a lixeira")

    def mensagemCaminhao(self, conexao, mensagem):
        """
        Gerencia as mensagens para o Caminhao
        """
        #adiciona o caminhao na lista de caminhoes do sistema
        if mensagem['id'] not in self.__caminhoes: 
            self.__caminhoes[mensagem['id']] = conexao

        #executa uma acao para uma determinada lixeira
        if(mensagem['acao'] != '' and mensagem['idLixeira'] !=''):
            msg = json.dumps({'acao': mensagem['acao']}).encode("utf-8")
            #envia uma msg para a lixeira com a acao que ela deve executar
            self.__lixeiras[mensagem['idLixeira']][1].sendall(msg)

    def mensagemLixeira(self, conexao, mensagem):
        """
        Gerencia as mensagens para a Lixeira
        """
        if mensagem['id'] not in self.__lixeiras:
            self.__lixeiras[mensagem['id']] = [mensagem['objeto'], conexao]
        else:
            #se a conexao ja existir no dicionario da lixeira, altera as informacoes do objeto lixeira
            self.__lixeiras[mensagem['id']][0] = mensagem['objeto']
        #se tiver administradores conectados no servidor, quando tiver uma alteracao em uma lixeira, ele recebera
        """lixeiras = {}
        for lKey, lValue in self.__lixeiras.items():
            print(json.loads(lValue))"""
        if self.__adms.keys():
            #enviando todas as lixeiras para todos os adms conectados no servidor
            for adm_conectado in self.__adms.values():
                adm_conectado.sendall(json.dumps(str(self.__lixeiras)).encode("utf-8"))
        
s = Servidor()