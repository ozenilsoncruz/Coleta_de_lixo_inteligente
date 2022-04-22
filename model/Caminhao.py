#from time import sleep
from time import sleep
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

    def __init__(self, id, latitude, longitude):
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
        self.__latitude = latitude
        self.__longitude = longitude
        self.lixeira = {}
        
        self._msg['tipo'] = 'caminhao'
        self._msg['objeto'] = self.dadosLixeira()
        self._msg['id'] = self.__id
        self._msg['idLixeira'] = ''
        self._msg['statusColeta'] = ''
        self.enviarDados()
    
    def dadosLixeira(self):
        """
        Retorna informacoes sobre o objeto
        """

        return {
            "id": self.__id,
            "Latitude": self.__latitude, 
            "Longitude": self.__longitude, 
        }

    def receberDados(self):
        """
        Recebe a mensagem do servidor e realiza ações
        """
        try:
            while True:
                mensagem = super().receberDados()
                if(mensagem):
                    print(f'''\n
                =======================================
                LIXEIRA {mensagem['idLixeira']}
                =======================================
                
Latitude    |{mensagem['lixeira']['Latitude']}
Longitude   |{mensagem['lixeira']['Longitude']}
Status      |{mensagem['lixeira']['Status']}
Capacidade  |{mensagem['lixeira']['Capacidade']}
Lixo        |{mensagem['lixeira']['Total preenchido']}\n''')
                self.coletarLixeira(mensagem['idLixeira'])
        except Exception as ex:
            print("Erro ao receber dados => ", ex)

    def coletarLixeira(self, idLixeira):
        """
        Esvazia a lixeira
            @param lixeira: Lixera
                lixeira a ser esvaziada
        """
        mensagemStatus = f"O Caminhão {self.__id} irá coletar a lixeira {idLixeira}"
        print(mensagemStatus)

        self._msg['idLixeira'] = idLixeira
        self._msg['statusColeta'] = mensagemStatus
        
        self.enviarDados()

        sleep(2)

        mensagemStatus = f"Caminhão {self.__id} coletou a lixeira {idLixeira}"
        self._msg['statusColeta'] = mensagemStatus
        print(mensagemStatus)

        self.enviarDados()
        self._msg['idLixeira'] = ''

c = Caminhao(1, 10, 20)

c2 = Caminhao(2, 14, 21)