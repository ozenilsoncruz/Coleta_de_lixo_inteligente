class Usuario:
    """
    A class que representa os usuarios do sistema
        Atributos
        ----------
        id: int
            id do adm
        senha: int
            senha do adm
    """

    def __init__(self, id: int, senha: str):
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
        self.__id = id
        self.__senha = senha

    def getId(self):
        """
        Retorna o Id do adm
            @return id - int
        """
        return self.__id
    
    def getSenha(self):
        """
        Retorna a senha do adm
            @return senha - str
        """
        return self.__senha

    def setSenha(self, senha: str):
        """
        Altera a latirude da lixeira
            @param senha - str
                nova senha a ser adicionada
        """
        self.__senha = senha