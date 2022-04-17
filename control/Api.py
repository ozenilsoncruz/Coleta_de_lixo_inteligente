import json

"""
Este é um pacote que manipula as mensagens dos clientes no sevidor do sistema 
de coleta inteligente
Neste pacote sao tratados os seguintes clientes:
    Lixeira
    Administrador
    Caminhao

Novos clientes podem ser adicionados posteriormente...
"""

lixeiras, adms, caminhoes = {}, {}, {}

def mensagemAdm(conexao, mensagem):
    """
    Gerencia as mensagens para o Adm
    """
    #indicando que se trata de variaveis globais ao pacote
    global lixeiras, adms, caminhoes

    if mensagem['id'] not in adms: 
        print("Conectado com: ", mensagem['tipo'], mensagem['id'])
        adms[mensagem['id']] = conexao
        
        #envia todas as lixeiras para o adm
        todasAsLixeiras = {}
        for lKey, lValue in lixeiras.items():
            todasAsLixeiras[lKey] = lValue[0]
        msg = json.dumps(todasAsLixeiras).encode("utf-8")
        conexao.sendall(msg)
    
    if(mensagem['acao'] != ''):
        if lixeiras.keys():
            #se a acao e o id da lixeira nao estiverem vazios
            if(mensagem['idLixeira'] !='' and mensagem['idCaminhao'] ==''):
                if (lixeiras[mensagem['idLixeira']]): 
                    msg = json.dumps({'acao': mensagem['acao'], 'idLixeira': mensagem['idLixeira']}).encode("utf-8")
                    lixeiras[mensagem['idLixeira']][1].sendall(msg)
                
        if lixeiras.keys() and caminhoes.keys():
            #se a acao e o id da caminhao nao estiverem vazios
            if(mensagem['idCaminhao'] !='' and mensagem['idLixeira'] !=''):
                if(caminhoes[mensagem['idCaminhao']] and lixeiras[mensagem['idLixeira']]):
                    msg = json.dumps({'acao': mensagem['acao'], 'idLixeira': mensagem['idLixeira'], 'lixeira': lixeiras[mensagem['idLixeira']][0]}).encode("utf-8")
                    print(lixeiras[mensagem['idLixeira']][0])
                    caminhoes[mensagem['idCaminhao']].sendall(msg)
                else:
                    print("Não foi possível enviar a mensagem para esvaziar a lixeira")

def mensagemCaminhao(conexao, mensagem):
    """
    Gerencia as mensagens para o Caminhao
    """
    #indicando que se trata de variaveis globais ao pacote
    global lixeiras, caminhoes

    #adiciona o caminhao na lista de caminhoes do sistema
    if mensagem['id'] not in caminhoes: 
        print("Conectado com: ", mensagem['tipo'], mensagem['id'])
        caminhoes[mensagem['id']] = conexao

    #executa uma acao para uma determinada lixeira
    if(mensagem['acao'] != '' and mensagem['idLixeira'] !=''):
        msg = json.dumps({'acao': mensagem['acao']}).encode("utf-8")
        #envia uma msg para a lixeira com a acao que ela deve executar
        lixeiras[mensagem['idLixeira']][1].sendall(msg)

def mensagemLixeira(conexao, mensagem):
    """
    Gerencia as mensagens para a Lixeira
    """
    #indicando que se trata de variaveis globais ao pacote
    global lixeiras, adms

    if mensagem['id'] not in lixeiras:
        print("Conectado com: ", mensagem['tipo'], mensagem['id'])
        lixeiras[mensagem['id']] = [mensagem['objeto'], conexao]
    else:
        print(f"Atualizando dados da Lixeria {mensagem['id']}")
        #se a conexao ja existir no dicionario da lixeira, altera as informacoes do objeto lixeira
        lixeiras[mensagem['id']][0] = mensagem['objeto']

        #se o total de lixo for igual a capacidade da lixeira, ela entra na lista para coleta de prioridade
        #if(mensagem['objeto']['Total preenchido'] == mensagem['objeto']['Capacidade']):
            #lixeira = {mensagem['id']: mensagem['objeto']}
            #lixeirasColetarPrioridade.append(lixeira)

    #se tiver administradores conectados no servidor, quando tiver uma alteracao em uma lixeira, ele recebera
    if adms.keys():
        todasAsLixeiras = {}
        for lKey, lValue in lixeiras.items():
            todasAsLixeiras[lKey] = lValue[0]
        #enviando todas as lixeiras para todos os adms conectados no servidor
        for adm_conectado in adms.values():
            adm_conectado.sendall(json.dumps(todasAsLixeiras).encode("utf-8"))

def deletarCliente(conexao):
    """
    Deleta o cliente conectado no servidor
    """ 

    #indicando que se trata de variaveis globais ao pacote
    global lixeiras, adms, caminhoes
    
    #faz a verificacao em qual dicionario a conexao esta e a elimina
    for k, v in lixeiras.items():
        if(conexao in v):
            lixeiras.pop(k)
            return f"\nLixeira {k} desconectada\n"
        
    for k, v in caminhoes.items():
        if(conexao == v):
            caminhoes.pop(k)
            return f"\nCaminhao {k} desconectado\n"
    
    for k, v in adms.items():
        if(conexao == v):
            adms.pop(k)
            return f"\nAdministrador {k} desconectado\n"

    print(lixeiras, adms, caminhoes)