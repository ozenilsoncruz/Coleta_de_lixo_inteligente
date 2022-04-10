from Cliente import Cliente

class Caminhao(Cliente):
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
        senha: int
            senha do adm
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
            @param senha: int
                senha do adm
        
        """
        Cliente.__init__(self)
        self.__id = id
        
        self._msg['tipo'] = 'caminhao'
        self._msg['id'] = self.__id
        self._msg['acao'] = ''
        self._msg['idLixeira'] = ''
        self.enviarDados()
        
    
    def receberDados(self):
        """
        Recebe a mensagem do servidor e realiza ações
        """
        mensagem = super().receberDados()

        if(mensagem['acao'] == "esvaziar"):
            self.coletarLixeira()

    def proxLixeira(self, mensagem):
        """
        Informacoes da lixeira a ser coletada
            @param lixeira: Lixeira
                lixeira a ser coletada
        """
        print(mensagem)

    def coletarLixeira(self, idLixeira):
        """
        Esvazia a lixeira
            @param lixeira: Lixera
                lixeira a ser esvaziada
        """
        self._msg['acao'] = 'esvaziar'
        self._msg['idLixeira'] = idLixeira
        self.enviarDados()

        self._msg['acao'] = ''
        self._msg['idLixeira'] = ''

c = Caminhao()