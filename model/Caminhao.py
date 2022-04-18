#from time import sleep
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
        self.lixeira = {}
        
        self._msg['tipo'] = 'caminhao'
        self._msg['id'] = self.__id
        self._msg['acao'] = ''
        self._msg['idLixeira'] = ''
        self.enviarDados()
        
    def receberDados(self):
        """
        Recebe a mensagem do servidor e realiza ações
        """
        try:
            while True:
                mensagem = super().receberDados()
                if(mensagem):
                    if(mensagem['acao'] == "esvaziar"):
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
        self._msg['acao'] = 'esvaziar'
        self._msg['idLixeira'] = idLixeira
        
        print(self._msg)
        #sleep(10)
        self.enviarDados()

        print(f"Caminhão {self.__id} coletou a lixeira {idLixeira}")
        self._msg['acao'] = ''
        self._msg['idLixeira'] = ''

c = Caminhao(1)