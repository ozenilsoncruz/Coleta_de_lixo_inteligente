from Cliente import Cliente
import json

class Lixeira(Cliente):
    """
    A class que representa um dos clientes que se conectara ao servidor.
        Atributos
        ----------
        Host : str
            ip utilizado
        Port : int
            numero de porta
        sock : socket
            soquete
        latitude: int
            coordenada 1
        longitude: int
            coodenada 2
        capacidade: float
            capacidade total da lixeira
        bloqueado: boolean
            status de bloqueio da porta da lixeira (se pode ou nao receber lixo)
        lixo: int
            quantidade de lixo dentro da lixeira
    """

    def __init__(self, id, latitude: int, longitude: int, capacidade: float = 100, bloqueado: bool = False):
        """
        Metodo construtor
            @param Host : str
                ip utilizado
            @param Port : int
                numero de porta
            @param latitude: int
                coordenada 1
            @param longitude: int
                coodenada 2
            @param capacidade: float
                capacidade total da lixeira
            @param bloqueado: boolean
                status de bloqueio da porta da lixeira (se pode ou nao receber lixo)
            @param lixo: int
                quantidade de lixo dentro da lixeira
        
        """
        Cliente.__init__(self, Port=8080)
        self.__id = id
        self.__latitude = latitude
        self.__longitude = longitude
        self.__capacidade = capacidade #m³
        self.__bloqueado = bloqueado
        self.__lixo = 0

    def __str__(self):
        """
        Modifica a string de exibição do objeto lixeira
        """
        return {
            'ID': self.__id, 
            'PORT': self.__Port,
            'Status': self.__bloqueado,
            'Capacidade': self.__capacidade,
            'Total preenchido': self.__lixo
        }

    def bloquear(self):
        """
        Trava a porta da lixeira
        """  
        self.__bloqueado = True
        self.enviarDados(f"Lixeira {self.__id} bloquada")

    def desbloquear(self):
        """
        Destrava a porta da lixeira
            @return: boolean
                retorna True se a quantidade de lixo for menor que a capacidade
        """
        if(self.__capacidade > self.__lixo):
            self.__bloqueado = False
            return True
        return False

    def addLixo(self, lixo: int):
        """
        Adiciona lixo na lixeira até o permitido
            @param lixo: int
                quantidade de lixo adiconada
            @return: boolean
                retorna True se conseguir adionar lixo
        """
        if(self.__capacidade >= self.__lixo + lixo): #se a capacidade de lixo nao for excedida, o lixo é adicionado
            self.__lixo += lixo
            if(self.__capacidade == self.__lixo): #se a capacidade de lixo chegar ao limite, o lixo e bloqueado
                self.bloquear()
                self.enviarDados(f"Lixeira {id} cheia")
            return True
        return False

    def esvaziarLixeira(self):
        """
        Redefine a quantidade de lixo dentro da lixeira
        """
        if self.__lixo == 0:
            return False
        else:            
            if(self.__capacidade == self.__lixo):
                self.__lixo == 0
                self.desbloquear()
            self.__lixo = 0
            return True

    def getLatitude(self):
        """
        Retorna a latitude da lixeira
            @return latitude - int
        """
        return self.__latitude
    
    def getLongitude(self):
        """
        Retorna a longitude da lixeira
            @return logitude - int
        """
        return self.__longitude
 
    def getCapacidade(self):
        """
        Retorna a capacidade da lixeira
            @return capacidade - float
        """
        return self.__capacidade
    
    def getBloqueado(self):
        """
        Retorna o status da lixeira
            @return bloquado - boolean
        """
        return self.__bloqueado

    def setLatitude(self, latitude):
        """
        Altera a latirude da lixeira
            @param latitude
                coordenada 1
        """
        self.__latitude = latitude

    def setLongitude(self, longitude):
        """
        Altera a longitude da lixeira
            @param longitude
                coordenada 2
        """
        self.__longitude = longitude
    
    def setCapacidade(self, capacidade):
        """
        Altera a capacidade da lixeira
            @param capacidade
                capacidade total da lixeira
        """
        self.__capacidade = capacidade

# l = Lixeira(15205, 25, 10)