from dic import *
def meu_index (lista,elemento):
    for i in range(len(lista)):
        if elemento == lista[i]:
             return i
    

def maior(lista):
    maior = lista[0]
    for i in range(len(lista)):
        if lista[i] >= maior:
            maior = lista[i]
    return maior


def menor (lista):
    menor = lista[0]
    for i in range(len(lista)):
        if lista[i] <= menor:
            menor = lista[i]
    return menor

def calculo_ntf(equipe):
    percentuais = [0.15, 0.12, 0.09, 0.06, 0.03, 0.0, -0.03, -0.06, -0.09, -0.12, -0.15]
    index = nfts[equipe][0] - 1
    preco = nfts[equipe][1] + (nfts[equipe][1] * percentuais[index])
    return preco
        


def forca_escolha(lista,msg, msg_erro = 'Inválido'):
    while True:
        escolha = input(msg)
        if escolha in lista:
            return escolha
        else:
            print("---------------------")
            print(msg_erro)
            print(lista)
            
def sair_continuar(msg,lista):    
    sair = forca_escolha(lista, msg)
    if sair == "sair":
        return False
    else:
        return True
    
#verifica a posicao que o usuario colocou em cada equipe para nao se repitir e ficar entre 1 e 11
def posicao(piloto, i, posicoes_usadas):
    while True:
        position = input(f"Digite a posição do piloto {piloto[i]} \n --> ")
        if position.isnumeric():
            position = int(position)
            if 1 <= position <= 11:
                if position not in posicoes_usadas:
                    posicoes_usadas.append(position)
                    return position
                else:
                    print("Esta posição já foi usada. Por favor, digite uma posição diferente.")
            else:
                print("Digite um valor entre 1 e 11.")
        else:
            print("Entrada inválida. Digite um número.")

# Verificação do User
def login(msg, msg_pwd, dic):
    while True:
        user_login = input(msg + "\n -->")
        user_Pwd = input(msg_pwd + "\n -->")
        if user_login in dic.keys():
            print("Sucesso") 
                                    
            if user_Pwd == dic[user_login]:
                print('Suceesso')
                break
            else: 
                print('Senha inválida')
                continue
        else:
            print('Usuário inválido')
    return True

def print_dic(dic , cotacao = ' R$',valor = False,index_value = ''):
    if valor: 
        for key in dic.keys():
            print(f"{key}= {dic[key][0]}- Valor:R${dic[key][1]} ")
    else:        
        for key in dic.keys():
            print(f"{key}= {cotacao}{dic[key][index_value]}")
    
        
def numeric(msg, msg_erro="invalido!!"):
    while True:
        numero = input(msg)
        if numero == "":
            print(msg_erro)
            continue
        if numero.isnumeric():
            return int(numero)
        else:
            print(msg_erro)
    
def limpar_carrinho():
    carrinho['nft'].clear()
    carrinho['valor_total'] = 0


