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
        self.__listaLixeiras = []
        
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

        self._msg['acao'] = ''
        self._msg['idLixeira'] = ''

    def desbloquearLixeira(self, idLixeira):
        """
        Desloqueia a lixeira se possivel
        """
        self._msg['acao'] = 'desbloquear'
        self._msg['idLixeira'] = idLixeira
        self.enviarDados()

        self._msg['acao'] = ''
        self._msg['idLixeira'] = ''

    def receberDados(self):
        """
        Recebe a mensagem do servidor e realiza ações
        """
        mensagem = super().receberDados()
        print(mensagem)

a = Administrador(14)
while True:
    a.receberDados()
    acao = input("Digite uma acao: ")
    
    if(acao == 'bloquear'):
        a.bloquearLixeira(25)
    elif(acao == 'desbloquear'):
        a.desbloquearLixeira(25)
    else:
        a.esvaziarLixeira(25, 1)