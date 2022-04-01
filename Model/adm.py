from lixeira import Lixeira
from usuario import Usuario
from cliente import Cliente

class Administrador(Cliente, Usuario):
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

    def __init__(self, cpf: int, senha: str):
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
        Usuario.__init__(self, cpf, senha)

    def verLixeira(self):
        pass

    def verificarEstadoLixeiras(self):
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
        pass

    def desbloquearLixeira(self, id):
        """
        Desloqueia a lixeira se possivel
        """
        pass

