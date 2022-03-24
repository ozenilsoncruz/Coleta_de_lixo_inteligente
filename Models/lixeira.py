from xmlrpc.client import boolean

"""
Classe lixeira
"""
class Lixeira:

    #Metodo construtor
    def __init__(self, latitude: int, longetude: int, capacidade: float, bloqueado: boolean = False):
        self.__latitude = latitude
        self.__longetude = longetude
        self.__capacidade = capacidade #m³
        self.__bloqueado = bloqueado

    '''
    Trava a porta da lixeira
    '''
    def bloquear(self):
        self.__bloqueado = True

    '''
    Destrava a porta da lixeira
    '''
    def desbloquear(self):
        self.__bloqueado = False

    '''
    Retorna a latitude da lixeira
    '''
    def getLatitude(self):
        return self.__latitude

    '''
    Retorna a longetude da lixeira
    '''
    def getLongetude(self):
        return self.__longetude

    '''
    Retorna a capacidade da lixeira
    '''
    def getCapacidade(self):
        return self.__capacidade
    
    '''
    Retorna o status da lixeira
    '''
    def getBloqueado(self):
        return self.__bloqueado

    '''
    Altera a latirude da lixeira
    '''
    def setLatitude(self, latitude):
        self.__latitude = latitude

    '''
    Altera a longetude da lixeira
    '''
    def setLongetude(self, longetude):
        self.__longetude = longetude
    
    '''
    Altera a capacidade da lixeira
    '''
    def setCapacidade(self, capacidade):
        self.__capacidade = capacidade
