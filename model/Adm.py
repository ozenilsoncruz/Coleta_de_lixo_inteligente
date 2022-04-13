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
        self.caminhoes = {}

        self._msg['tipo'] = 'adm'
        self._msg['id'] = self.__id
        self._msg['acao'] = ''
        self._msg['idLixeira'] = ''
        self._msg['idCaminhao'] = ''
        #print(self._msg)
        self.enviarDados()
    
    def esvaziarLixeira(self, idLixeira, idCaminhao):
        """
        Adiciona uma lixeira que esta cheia a lista de lixeiras escolhidas pelo adm
        """
        self._msg['acao'] = 'esvaziar'
        self._msg['idLixeira'] = idLixeira
        self._msg['idCaminhao'] = idCaminhao
        self.enviarDados()

        print(f"Caminhão {idCaminhao} deve coletar a lixeira {idLixeira}")
        self._msg['acao'] = ''
        self._msg['idLixeira'] = ''
        self._msg['idCaminhao'] = ''

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
        dados = super().receberDados()
        if dados != None:
            self.lixeiras = dados
        print(self.lixeiras)
    
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
    Total preenchido |{lixeira['Capacidade']}

                    \n'''
                )
                
a = Administrador(1)
acao = ''

while acao != 'sair':

    a.receberDados()
    acao = input(
    """\n
================================
    [b] - Bloquear
    [d] - Desbloquear
    [e] - Esvaziar
    [l] - Lixeiras no sistema
================================
    
    Digite uma acao: """).lower().strip()[0]
    
    if(acao == "b" or acao == "d" or acao == "e"):
        try:
            lixeira = str(input("Qual lixeira: "))
            if(acao == 'b'):
                a.bloquearLixeira(lixeira)
            elif(acao == 'd'):
                a.desbloquearLixeira(lixeira)
            elif(acao == 'e'):
                a.esvaziarLixeira(lixeira, 1)
        except:
            print("Informe uma opção válida!")
            acao = ''
    elif(acao == 'l'):
        condicao = True
        while condicao:
            print(
                """\n
=========================
        No sitema:
=========================
            """)
            for idL in a.lixeiras.keys():
                print(f"Lixeira -> {idL}")
            id = input("\nInforme o id da lixera que deseja exibir: ")
            if(a.lixeiras[id]):
                a.informacaoLixeira(id)
                condicao = False
            else:
                print("Informe um id válido!")