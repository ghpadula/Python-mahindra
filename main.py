from dic import *
from func import *

opcoes_Inicio = ["1","2","3","4"]
user = False
admin = False

while True:
    while True:
        print("Seja bem vindo a TechAdvanced: ")
        #print("Voce deseja fazer \n -->(1)Login \n -->(2)Cadastrar \n -->(3)Login como administrador \n -->(4)Sair")
        escolha_inicio = forca_escolha(opcoes_Inicio,"Voce deseja fazer \n -->(1)Login \n -->(2)Cadastrar \n -->(3)Login como administrador \n -->(4)Sair \n -->")
        match escolha_inicio:
            case "1":
                user = login('Digite seu Usuário', 'Digite sua senha', usuarios)
                #is_adm = False
                break
            case '2':
                newUser = input("Digite o nome de usuario que deseja cadastrar: \n -->")
                newPwd = input(f"Digite a senha de login do usuario {newUser}\n --> ")
                usuarios[newUser] = newPwd
                print("Voce voltara ao inicio, digite 1 para realizar o login \n Obrigado por se cadastrar no TechAdvanced!")
            case '3':
                admin = login('Digite seu Usuário', 'Digite sua senha', adm)
                break
            #is_adm = True
            case '4':
                print('Obrigado por utilizar TechAdvanced!')
                exit()

        
    if user:
        admin = False
        user = False
        while True:
            print(f"Bem vindo ao portal do Usario senhor {user}")
            escolha = forca_escolha(['1','2','3','4','5','6'], "Digite:\n [1] para ver os preços de nft de cada Equipe \n [2] Para visualizar a posição das equipes na ultima corrida \n [3] Para comprar nft \n [4] Exibir carrinho \n [5] Para exibir suas NFTs\n [6] Para sair\n -->")
            match escolha:
                case '1':
                    while True:
                        print_dic(nfts,'R$',False,1)
                        if sair_continuar("Digite 'voltar' para voltar ao Menu\n --> ",['voltar']):
                            break

                case '2':
                    while True:
                        print_dic(nfts,'',False,0)
                        if sair_continuar("Digite 'voltar' para voltar ao Menu\n --> ",['voltar']):
                                break

                case '3':
                    while True:     
                        comprar = forca_escolha(["sim","nao"],"Deseja comprar alguma nft? \n -->")
                        if comprar == "nao":
                            break
                        print_dic(nfts, 1)           
                        nft_Buy = forca_escolha(nfts.keys(),"De qual equipe voce deseja comprar a nft? \n -->")
                        qtd = numeric("Digite a quandidade que deseja comprar \n --> ")
                        carrinho['nft'][nft_Buy] = qtd
                        carrinho['valor_total'] += carrinho['nft'][nft_Buy] * nfts[nft_Buy][1]
                        print(carrinho['valor_total'])
                        #print(carrinho)
                                            
                        if sair_continuar("Digite [sair] para sair e [continuar] para continuar comprando \n -->",["sair","continuar"]):
                            continue
                        else:
                            break
                    
                case '4':
                    for key in carrinho['nft'].keys():
                        print("Voce esta comprando: ")
                        print(f"{key} = {carrinho['nft'][key]}")
                    print(f"Valor Total = {carrinho['valor_total']}")
                    if sair_continuar("Digite sair para sair do carrinho \n -Digite comprar para comprar",["sair","comprar"]):
                        for key in carrinho['nft'].keys():
                                if key in carteira_usuario['nft']:
                                    carteira_usuario['nft'][key] += carrinho['nft'][key]
                                else:
                                    carteira_usuario['nft'][key] = carrinho['nft'][key]
                        limpar_carrinho()
                        print("Compra efetuada com sucesso, seu carrinho foi esvaziado!")
                        print(carrinho)
                        
                
                case '5': 
                    while True:
                        for key in carteira_usuario['nft']:
                            print(f"{key} = {carteira_usuario['nft'][key]} unidades")
                        if sair_continuar("Digite 'voltar' para voltar ao Menu\n --> ",['voltar']):
                            break
                case '6':
                    break 

    if admin:
        admin = False
        user = False
        while True:
            print(f"Bem-vindo ao portal do usuário, senhor {user}")
            escolha = forca_escolha(['1', '2'], "Digite:\n [1] Alterar posição das equipes na última corrida (Muda automaticamente os preços das NFT)\n [2] Para sair\n --> ")
            
            match escolha:
                case '1':
                    alterar = forca_escolha(['sim', 'nao'], "Você deseja trocar as posições das equipes? sim ou nao\n --> ")
                    if alterar == 'sim':
                        posicoes_usadas = []
                        for key in nfts:
                            while True:
                                posicao = numeric(f"Digite a posição da equipe {key} (1 a 11): \n -->")
                                
                                if posicao in range(1, 12):
                                    if posicao not in posicoes_usadas:
                                        posicao_antiga = nfts[key][0]
                                        posicoes_usadas.append(posicao)
                                        nfts[key][0] = posicao                                        
                                        nova_preco = calculo_ntf(key)                                        
                                        nfts[key][1] = nova_preco 
                                        print(f"A posição da {key} foi alterada de {posicao_antiga}º para {nfts[key][0]}º e o novo valor é R${nfts[key][1]} ")                                
                                        
                                        break
                                    else:
                                        print("Essa posição já está ocupada. Tente outra.")
                                else:
                                    print("Entrada inválida. Por favor, digite um número entre 1 e 11.")
                        print_dic(nfts,'',True)
                        print("Novos valores após a alteração!")
                case '2':
                    break

#formatar alguns prints e adicionar saida no adm
    
#if admin:
   # print("Logado com adm")    
    
    






