from Cliente import Cliente

class Administrador(Cliente):
    """
    A class que representa o administrador, um dos clientes que se conectara ao servidor.
        Atributos
        ----------
        Host : str
            ip utilizado
        Port : int
            numero de porta
        sock : socket
            soquete
        id: int
            id do adm
    """

    def __init__(self, id):
        """
        Metodo construtor
            @param Host : str
                ip utilizado
            @param Port : int
                numero de porta
            @param id: int
                id do adm
        """
        Cliente.__init__(self)
        self.__id = id
        self.lixeiras = {}
        self.caminhoes = []
        self.ordem = []

        self._msg['tipo'] = 'adm'
        self._msg['id'] = self.__id
        self._msg['acao'] = ''
        self._msg['idLixeira'] = ''
        self._msg['statusColeta'] = ''
        self._msg['ordem'] = []
        #print(self._msg)
        self.enviarDados()
    
    def coletarLixeira(self, idLixeira):
        """
        Adiciona uma lixeira que esta cheia a lista de lixeiras escolhidas pelo adm
        """   
        self._msg['acao'] = 'coletar'
        self._msg['idLixeira'] = idLixeira
        self.enviarDados()
        print(f"A lixeira {idLixeira} foi adicionada a lista de coleta")
        self._msg['acao'] = ''
        self._msg['idLixeira'] = ''
        
    def bloquearLixeira(self, idLixeira):
        """
        Bloqueia a lixeira para que nao receba mais lixo
        """
        self._msg['acao'] = 'bloquear'
        self._msg['idLixeira'] = idLixeira
        self.enviarDados()

        print(f"Bloquear a lixeira {idLixeira}")
        self._msg['acao'] = ''
        self._msg['idLixeira'] = ''

    def desbloquearLixeira(self, idLixeira):
        """
        Desloqueia a lixeira se possivel
        """
        self._msg['acao'] = 'desbloquear'
        self._msg['idLixeira'] = idLixeira
        self.enviarDados()

        print(f"Desbloquear a lixeira {idLixeira}")
        self._msg['acao'] = ''
        self._msg['idLixeira'] = ''

    def receberDados(self):
        """
        Recebe a mensagem do servidor e realiza ações
        """
        try:
            while True:
                mensagem = super().receberDados()
                if(mensagem != None):
                    if(mensagem['statusColeta'] != ''):
                        print(mensagem['statusColeta'])
                    self.lixeiras = mensagem['lixeiras']
                    self.caminhoes = mensagem['caminhoes']
                    self.ordem = mensagem['ordem']
        except Exception as ex:
            print("Erro ao receber dados => ", ex)
            
    def informacaoLixeira(self, idLixeira):
        """
        Exibe as informações de uma lixeira informada
        """
        lixeira = self.lixeiras[idLixeira]
        print(
                    f'''\n
=======================================
LIXEIRA {idLixeira}
=======================================

    Latitude         |{lixeira['Latitude']}
    Longitude        |{lixeira['Longitude']}
    Status           |{lixeira['Status']}
    Capacidade       |{lixeira['Capacidade']}
    Total preenchido |{lixeira['Capacidade']}\n''')

    def alteraOrdem(self, id, novaPosicao):
        """
        Altera a ordem de coleta das lixeiras
        """
        if(id in self.ordem and novaPosicao !=""):
            self.ordem.remove(id)
            self.ordem.insert(novaPosicao, id)
            self._msg['ordem'] = self.ordem
        else:
            self._msg['ordem'] = []
        self.enviarDados()

a = Administrador(1)
acao = ''

while acao != 'sair':
    try:
        acao = input("""\n================================
    [1] - Bloquear
    [2] - Desbloquear
    [3] - Coletar lixeira
    [4] - Ordem de coleta
    [5] - Lixeiras no sistema
================================
    
    Digite uma acao: """)
        if(acao == "1" or acao == "2" or acao == "3"):
            lixeira = input("Qual lixeira: ")
            if(lixeira in a.lixeiras):
                if(acao == '1'):
                    a.bloquearLixeira(lixeira)
                elif(acao == '2'):
                    a.desbloquearLixeira(lixeira)
                elif(acao == '3'):
                    if(lixeira not in a.ordem):
                        a.coletarLixeira(lixeira)
                    else:
                        print('Lixeira já está na lista para ser coletada!')
            else:
                print('Lixeira não existe')
        elif( acao == "4" or acao == "5"):
            if(acao == "5"):
                print("""\n=========================
    No sitema:
=========================""")
                for idL in a.lixeiras.keys():
                    print(f"Lixeira -> {idL}")
                id = input("\nInforme o id da lixera que deseja exibir: [voltar]").strip()
                if(id == 'v' or id == "voltar"):
                    continue
                elif(a.lixeiras.get(id)):
                    a.informacaoLixeira(id)
                else:
                    print("Informe um id válido!")
            else:
                if(len(a.ordem) != 0):
                    print("Ordem de coleta:\n", a.ordem)
                    tipoOrdem = input("\nInforme o tipo de coleta: [m/manual, t/total de lixo]: ").lower().strip()[0]
                    if(tipoOrdem == "m"):
                        id = input("\nInforme o id da lixera que deseja alterar a ordem de coleta: ").strip()
                        if(id in a.ordem):
                            try:
                                novaPosicao = int(input(f"\nInforme a nova posição na ordem de coleta: [Entre 1 e {len(a.ordem)}] "))
                                if(0 < novaPosicao <= len(a.ordem)):
                                    a.alteraOrdem(id, novaPosicao-1)
                                else:
                                    print("Valor não está na faixa da lista")
                            except:
                                print("Informe um número inteiro!")
                        else:
                            print("Lixeira não está na ordem de coleta!")
                    elif(tipoOrdem == "t"):
                        a.alteraOrdem("", "")
                    else:
                        print("Escolha uma opção")
                else:
                    print("Não há lixeiras no momento")
        else:
            print("Informe uma opção válida!")
    except:
        print("Informe uma opção válida!")