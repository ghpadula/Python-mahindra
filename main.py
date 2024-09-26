from dic import *
from func import *


opcoes_Inicio = ["1","2","3","4"]
user = False
admin = False

while True:
    while True:
        print("Seja bem vindo a TechAdvanced: ") 
        escolha_inicio = forca_escolha(opcoes_Inicio,"Voce deseja fazer \n -->(1)Login \n -->(2)Cadastrar \n -->(3)Login como administrador \n -->(4)Sair \n -->")
        match escolha_inicio:
            case "1":
                user = login('Digite seu Usuário', 'Digite sua senha', usuarios)
                break
            case '2':
               cadastro()
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
            print(f"Bem vindo ao portal do Usuário")
            escolha = forca_escolha(['1','2','3','4','5','6'], "Digite:\n [1] para ver os preços de nft de cada Equipe \n [2] Para visualizar a posição das equipes na ultima corrida \n [3] Para comprar nft \n [4] Exibir carrinho \n [5] Para exibir suas NFTs\n [6] Para sair\n -->")
            match escolha:
                case '1':
                    while True:
                        print_dic(nfts,1, True)
                        if sair_continuar("Digite 'voltar' para voltar ao Menu\n --> ",['voltar']):
                            break

                case '2':
                    while True:
                        print_dic(nfts,0)
                        if sair_continuar("Digite 'voltar' para voltar ao Menu\n --> ",['voltar']):
                                break

                case '3':
                    adicionar_carrinho()
                case '4':
                    comprar_carrinho()
                        
                
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
            print(f"Bem-vindo ao portal da Administração")
            escolha = forca_escolha(['1', '2'], "Digite:\n [1] Alterar posição das equipes na última corrida (Muda automaticamente os preços das NFT)\n [2] Para sair\n --> ")
            
            match escolha:
                case '1':
                    adm_trocar_posicao()
                case '2':
                    break


    
    






