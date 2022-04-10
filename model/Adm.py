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
        Cliente.__init__(self, Port=8082)
        self.__id = id
        self.enviarDados({'id': self.__id})
    
    def verificarEstadoLixeiras(self):
        """
        Verifica o estado da lixeira 
        """
        pass

    def lixeiraColeta(self):
        """
        Adiciona uma lixeira que esta cheia a lista de lixeiras escolhidas pelo adm
        """
        pass

    def bloquearLixeira(self, id):
        """
        Bloqueia a lixeira para que nao receba mais lixo
        """
        self.enviarDados()

    def desbloquearLixeira(self, id):
        """
        Desloqueia a lixeira se possivel
        """
        pass

    def receberDados(self):
        """
        Recebe a mensagem do servidor e realiza ações
        """
        mensagem = super().receberDados()
        print(mensagem.decode())

a = Administrador(14)

a.receberDados()