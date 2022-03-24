import socket

class Servidor:

    def __int__(self):
        self.__Host = 'localhost' #ip utilizado
        self.__Port = 50000 #numero de porta

        #objeto do tipo socket que contem a familia de protocolo e o tipo de procolo a ser utilizado
        #AF_INET para ipv4
        #SOCK_STREAM para conexao do tipo TCP
        self.__sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        #o metodo bind associa o socket servidor a um endereço 
        self.__sock.bind((self.__Host, self.__Port)) 

        #o metodo listen começa a escutar os pedidos de conexao, recebe como parametro o limite de conexoes
        self.__sock.listen()
        print('Aguardando...')

        #o metodo accept aceita a conexao de um cliente e retorna a conexao e o endereco
        conexao, endereco = sock.accept()
        print('Conectado em ', endereco)

        #Troca de mensagens
        while True:
            #o metodo aguarda um dado enviado pela rede de até 1024 Bytes
            dados = conexao.recv(1024)

            #quando os dados forem recebidos
            if not dados:
                print('Fechando conexão...')
                conexao.close()
                break
            
            #envia os dados de volta para o cliente
            conexao.sendall(dados)