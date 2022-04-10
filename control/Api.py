class Api:
    
    def __init__(self, ip, port):
        self.IP = ip
        self.PORT = port
        self.BASE_URL = self.IP + '/' + str(self.PORT)
        
    
    def fetchMessage(self,data,client, lixeiras):
        message = data['message']
        print('API: ', message, client)
        if 'data' in data: data = data['data']
        
        ##### LIXEIRA BALANCER #####        
        if message == 'lixeira/emptyLixeira':
            self.emptyLixeira(client,message,data)
            
        elif message == 'lixeira/fullLixeira':
            self.fullLixeira(client,message,data)
            
        elif message == 'lixeira/alertLixeiraLimit':
            self.alertLixeiraLimit(client,message,data)

        elif message == 'lixeira/lockLixeira':
            self.lockLixeira(client,message,data)
        
        elif message == 'lixeira/unlockLixeira':
            self.unlockLixeira(client,message,data)    
        ##### LIXEIRA BALANCER #####
        
        
        ##### CENTRAL BALANCER #####        
        elif message == 'central/addLixo':
            self.addLixo(client,data)
    
        elif message == 'central/removeLixo':
            self.removeLixo(client,message,data)
            
        elif message == 'central/lixeiras':
            self.getAllLixeiras(lixeiras)

        elif message == 'central/LockLixeira':
            self.centralLockLixeira(client,message,data)
        
        elif message == 'central/unLockLixeira':
            self.centralUnlockLixeira(client,message,data)    
        ##### CENTRAL BALANCER #####

    
    
    ##### LIXEIRA METHODS #####
    def emptyLixeira(self,client,message,data):
        print(client,message,data)
    
    def fullLixeira(self,client,message,data):
        print(client,message,data)
        
    def alertLixeiraLimit(self,client,message,data):
        print(client,message,data)
        
    def lockLixeira(self,client,message,data):
        print(client,message,data)
        
    def unlockLixeira(self,client,message,data):
        print(client,message,data)
    ##### LIXEIRA METHODS #####
    
    
    ##### CENTRAL METHODS #####
    def addLixo(self,client,data):
        # tratar dado aqui
        # lixeiraIP, lixeiraID
        print('Lixo Adicionado')
        
    def removeLixo(self):
        print('Lixo Removido')
        
    def getAllLixeiras(self,lixeiras):
        print('Todas as Lixeiras: ',lixeiras)
        return lixeiras
        
    def centralLockLixeira(self):
        print('Lixeira travada')
        
    def centralUnlockLixeira(self):
        print('Lixeira destravada')