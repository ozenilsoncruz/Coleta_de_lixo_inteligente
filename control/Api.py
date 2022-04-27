import json
from math import dist, sqrt

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

#ids das lixeiras a serem coletadas por ordem de prioridade
ordem = []

def mensagemAdm(conexao, mensagem):
    """
    Gerencia as mensagens para o Adm
    """
    #indicando que se trata de variaveis globais ao pacote
    global lixeiras, adms, caminhoes, ordem

    if mensagem['id'] not in adms: 
        print("Conectado com: ", mensagem['tipo'], mensagem['id'])
        adms[mensagem['id']] = conexao
        __enviarMsgAdm(conexao)
    
    if(mensagem['acao'] != ''):
        
        if lixeiras.keys():
            #se a acao e o id da lixeira nao estiverem vazios
            if(mensagem['idLixeira'] !=''):
                if (mensagem['acao'] != 'coletar' and lixeiras[mensagem['idLixeira']]): 
                    msg = json.dumps({'acao': mensagem['acao'], 'idLixeira': mensagem['idLixeira']}).encode("utf-8")
                    lixeiras[mensagem['idLixeira']][1].sendall(msg)

                if(mensagem['acao'] == 'coletar' and lixeiras[mensagem['idLixeira']] and mensagem['idLixeira'] not in ordem):
                    #se a lixeira que o adm enviou não estiver vazia ela sera adicionada na lista para coleta
                    if(lixeiras[mensagem['idLixeira']][0]['Total preenchido'] != '0,00%'):
                        ordem.append(mensagem['idLixeira'])
                
    if(len(mensagem['ordem']) != 0):
        #atualiza a ordem de coleta para a coleta manual do adm
        ordem = mensagem['ordem']
    else:
        ordem =  __ordemColeta()

    #se o adm enviar um id de alguma lixeira, essa lixeira entrara no final da lista de coleta
    if(mensagem['idLixeira'] != ''):
        if(lixeiras[mensagem['idLixeira']]):
            ordem.append(mensagem['idLixeira'])
        #atualiza todos os adms sobre as alteracores realizadas
    
    print(ordem)
    __enviarMsgTodosAdms()
    __enviarMsgCaminhao()

def mensagemCaminhao(conexao, mensagem):
    """
    Gerencia as mensagens para o Caminhao
    """
    #indicando que se trata de variaveis globais ao pacote
    global lixeiras, caminhoes, ordem

    #adiciona o caminhao na lista de caminhoes do sistema
    if mensagem['id'] not in caminhoes: 
        print("Conectado com: ", mensagem['tipo'], mensagem['id'])
        caminhoes[mensagem['id']] = [mensagem['objeto'], conexao]
        #envia para o caminhao a lixeira que ele deve coletar
        if(len(ordem) > 0):
            id = ordem.pop(0)
            msg = json.dumps({'acao': 'esvaziar'}).encode("utf-8")
            lixeiras[id][1].sendall(msg)
    else:
        print("to no else")
        msg = json.dumps({'acao': 'esvaziar'}).encode("utf-8")
        lixeiras[mensagem['idLixeira']][1].sendall(msg)


    print(mensagem['statusColeta'])
    #se tiver administradores conectados no servidor, quando tiver uma alteracao em uma lixeira, ele recebera
    __enviarMsgTodosAdms(mensagem['statusColeta'])

def mensagemLixeira(conexao, mensagem):
    """
    Gerencia as mensagens para a Lixeira
    """
    #indicando que se trata de variaveis globais ao pacote
    global lixeiras, caminhoes, adms, ordem

    if mensagem['id'] not in lixeiras:
        print("Conectado com: ", mensagem['tipo'], mensagem['id'])
        lixeiras[mensagem['id']] = [mensagem['objeto'], conexao]
    else:
        print(f"\nAtualizando dados da Lixeria {mensagem['id']}")
        #se a conexao ja existir no dicionario da lixeira, altera as informacoes do objeto lixeira
        lixeiras[mensagem['id']][0] = mensagem['objeto']

        #se o total de lixo tiver atingido 100% a lixeira será bloquada automaticamente
        if(mensagem['objeto']['Total preenchido'] == "100.00%" and mensagem['objeto']['id'] not in ordem):
            ordem.append(mensagem['objeto']['id'])
            __enviarMsgCaminhao()
               
    #se tiver administradores conectados no servidor, quando tiver uma alteracao em uma lixeira, ele recebera
    __enviarMsgTodosAdms()

def deletarCliente(conexao):
    """
    Deleta o cliente conectado no servidor
    """ 
    #indicando que se trata de variaveis globais ao pacote
    global lixeiras, adms, caminhoes, ordem
    
    #faz a verificacao em qual dicionario a conexao esta e a elimina
    for k, v in lixeiras.items():
        if(conexao in v):
            lixeiras.pop(k)
            #envia a lista atualizada com todas as lixeiras para os adms
            #enviando todas as lixeiras para todos os adms conectados no servidor
            if(k in ordem):
                ordem.remove(k)
            __enviarMsgTodosAdms()
            return f"\nLixeira {k} desconectada\n"
        
    for k, v in caminhoes.items():
        if(conexao == v):
            caminhoes.pop(k)
            #envia a lista atualizada com todas os caminhoes para os adms
            __enviarMsgTodosAdms()
            return f"\nCaminhao {k} desconectado\n"
    
    for k, v in adms.items():
        if(conexao == v):
            adms.pop(k)
            return f"\nAdministrador {k} desconectado\n"

def __ordemColeta():
    """
    Organiza a ordem de coleta por parte do adm
    """
    global ordem, lixeiras

    listaOrdenada = []
    for lK, lV in lixeiras.items():
        if(lK in ordem):
            listaOrdenada.append((lK, lV[0]['Total preenchido']))

    # listaOrdenada.reverse(key=lambda x: x[1])
    sorted(listaOrdenada, key=lambda l:l[1], reverse=True)

    lista = []
    for l in listaOrdenada:
        lista.append(l[0])

    return lista

def __selecionaCaminhao(l):
    """
    Seleciona o caminhao mais proximo da lixeira em questao
    """
    global caminhoes
    cam = list(caminhoes.values())
    caminhaoMaisProx = cam[0][0]
    a = (l['Latitude'], l['Longitude'])

    for caminhao in caminhoes.values():    
        b = (caminhao[0]['Latitude'], caminhao[0]['Longitude'])
        c = (caminhaoMaisProx['Latitude'], caminhaoMaisProx['Longitude'])
        
        if (dist(a, b) < dist(a, c)):
           caminhaoMaisProx = caminhao[0]
    return caminhaoMaisProx['id']

def __listaLixeiras(lixeiras):
    """
    Retorna apenas as informacoes das lixeiras sem a conexao
    """
    todasAsLixeiras = {}
    for lKey, lValue in lixeiras.items():
        todasAsLixeiras[lKey] = lValue[0]
    return todasAsLixeiras

def __enviarMsgAdm(conexao, mensagem=""):
    """
    Envia mensagem para um administrador conecatado
    """
    #envia a lista atualizada com todas as lixeiras para os adms
    global lixeiras, adms, caminhoes, ordem

    c = []
    if(caminhoes.keys()):
        c = list(caminhoes.keys())
    msg = json.dumps({'caminhoes': c, 'lixeiras': __listaLixeiras(lixeiras), 'ordem': ordem, 'statusColeta': mensagem}).encode("utf-8")
    conexao.sendall(msg)

def __enviarMsgTodosAdms(mensagem = ""):
    """
    Envia mensagem para todos os adms conectados
    """
    #envia a lista atualizada com todas os caminhoes para os adms
    if adms.keys():
        #enviando todas as lixeiras para todos os adms conectados no servidor
        for adm_conectado in adms.values():
            __enviarMsgAdm(adm_conectado, mensagem)

def __enviarMsgCaminhao():
    """
    Envia mensagem para um caminhao conecatado
    """
    global ordem

    if(caminhoes and len(ordem) > 0):
        id = ordem.pop(0)
        l = lixeiras[id][0]
        c = __selecionaCaminhao(l)
        
        msg = json.dumps({'idLixeira': id, 'lixeira': l}).encode("utf-8")
        caminhoes[c][1].sendall(msg)