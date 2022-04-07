from Usuario import Usuario
from Cliente import Cliente

class Caminhao(Cliente, Usuario):
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
        Cliente.__init__(self, Port=8081)
        Usuario.__init__(self, id, senha)
    
    def proxLixeira(self):
        """
        Informacoes da lixeira a ser coletada
            @param lixeira: Lixeira
                lixeira a ser coletada
        """
        pass

    def coletarLixeira(self):
        """
        Esvazia a lixeira
            @param lixeira: Lixera
                lixeira a ser esvaziada
        """
        pass