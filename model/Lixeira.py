from time import sleep
from Cliente import Cliente

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

    def __init__(self, id, latitude: int, longitude: int, capacidade: float = 100, bloqueado: bool = False, ip : str = '127.0.0.1'):
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
        Cliente.__init__(self, ip, 50000)
        self.__id = id
        self.__latitude = latitude
        self.__longitude = longitude
        self.__capacidade = capacidade #m³
        self.__bloqueado = bloqueado
        self.__lixo = 0

        self._msg['tipo'] = 'lixeira'
        self._msg['id'] = self.__id
        self._msg['objeto'] = self.dadosLixeira()
        self.enviarDados()

    def dadosLixeira(self):
        """
        Retorna informacoes sobre o objeto
        """
        if(self.__bloqueado == True):
            status = "Bloqueada"
        else:
            status = "Desbloqueada"

        return {
            "id": self.__id,
            "Latitude": self.__latitude, 
            "Longitude": self.__longitude, 
            "Status": status, 
            "Capacidade": self.__capacidade, 
            "Total preenchido": f'{self.getPorcentagem()*100:.2f}'+'%'
        }
        
    def receberDados(self):
        """
        Recebe a mensagem do servidor e realiza ações
        """
        try:
            while True:
                mensagem = super().receberDados()
                if(mensagem):
                    print('MENSAGEM: ', mensagem)
                    if(mensagem['acao'] == "esvaziar"):
                        print("Esvaziando Lixeira...")
                        self.esvaziarLixeira()
                    elif(mensagem['acao'] == "bloquear"):
                        print("Bloqueando Lixeira...")
                        self.bloquear()
                    elif(mensagem['acao'] == "desbloquear"):
                        print("Desbloqueando Lixeira...")
                        self.desbloquear()
        except Exception as ex:
            print("Erro ao receber dados => ", ex)

    def bloquear(self):
        """
        Trava a porta da lixeira
        """  
        self.__bloqueado = True
        self._msg['objeto'] = self.dadosLixeira()
        self.enviarDados()
        print(f"Lixeira {self.__id} BLOQUEADA")

    def desbloquear(self):
        """
        Destrava a porta da lixeira
            @return: boolean
                retorna True se a quantidade de lixo for menor que a capacidade
        """
        if(self.__capacidade > self.__lixo):
            self.__bloqueado = False
            print(f"Lixeira {self.__id} DESBLOQUEADA")
            #retorna nova informacao sobre o objeto
            self._msg['objeto'] = self.dadosLixeira()
            self.enviarDados()
        
        else:
            print(f"Lixeira Cheia! Impossível desbloquear Lixeira {self.__id}")


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
                self.__bloqueado = True
        self._msg['objeto'] = self.dadosLixeira()
        self.enviarDados()

    def esvaziarLixeira(self):
        """
        Redefine a quantidade de lixo dentro da lixeira
        """
        if(self.__bloqueado == True):
            self.__bloqueado = False
        self.__lixo = 0

        #retorna nova informacao sobre o objeto
        self._msg['objeto'] = self.dadosLixeira()
        self.enviarDados()
        
        print(f"Lixeira {self.__id} ESVAZIADA")

    def setLatitude(self, latitude):
        """
        Altera a latirude da lixeira
            @param latitude
                coordenada 1
        """
        self.__latitude = latitude
        self._msg['objeto'] = self.dadosLixeira()
        self.enviarDados()

    def setLongitude(self, longitude):
        """
        Altera a longitude da lixeira
            @param longitude
                coordenada 2
        """
        self.__longitude = longitude
        self._msg['objeto'] = self.dadosLixeira()
        self.enviarDados()
    
    def setCapacidade(self, capacidade):
        """
        Altera a capacidade da lixeira
            @param capacidade
                capacidade total da lixeira
        """
        self.__capacidade = capacidade
        self._msg['objeto'] = self.dadosLixeira()
        self.enviarDados()
 
    def getId(self):
        """
        Retorna ID da lixeira
            @return latitude - str
        """
        return self.__id
 
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
 
    def getPorcentagem(self):
        """
        Retorna a porcentagem de lixo da lixeira
            @return porcentagem - float
        """
        return self.__lixo/self.__capacidade
 
    def getLixo(self):
        """
        Retorna o lixo da lixeira
            @return lixo - int
        """
        return self.__lixo
 
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
