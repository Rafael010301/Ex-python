lista_de_espera = []
contador_de_chamados = 0
opcao = -1
while opcao != "fechar":
    print("--- MENU ---")
    print("OPÇÕES ...")
    print("Opção 1 adicionar um cliente no fim da fila")
    print("Opção 2 chamar o próximo cliente o primeiro da fila")
    print("Opção 3 desistência remover um cliente específico pelo nome")
    print("Opção 4 mostrar a fila de espera atual")
    print("Opção 5 fechar o restaurante e encerrar o programa (fechar )")
    print()
    # parte de escolha 
    opcao = input("O que você pretende fazer ? (caso queira fechar digite 'fechar' )\n")
    #1° OPÇÃO 
    if opcao == "1":
        nome = input("Qual o nome do novo cliente a ser adicionado ? \n").lower()
        if nome in lista_de_espera:
            print("O nome já existe aqui na lista !")
            print()
        else:
            lista_de_espera.append(nome)
            print("Cliente adicionado à fila de espera")
            print()
    # 2° OPÇÃO 
    elif opcao == "2":
        print("Chamando primeiro cliente ... ")
        if len(lista_de_espera) == 0:
            print("Não ha ninguem na fila ! ")
            print()
        else:
            cliente_atendido = lista_de_espera.pop(0)
            print(f"Esse é o primeiro cliente : {cliente_atendido} ")
            contador_de_chamados += 1 
    # 3° OPÇÃO 
    elif opcao == "3":
        cliente_removido = input("Digite o nome do cliente à ser removido : \n").lower()
        print()
        if cliente_removido in lista_de_espera:
            lista_de_espera.remove(cliente_removido)
        else:
            print("Esse cliente não existe !!! ")
            print()
    #4° OPÇÃO 
    elif opcao == "4":
        if len(lista_de_espera) == 0: # CASO ESTEJA VAZIO !!!
            print("LISTA VAZIA !!!")
            print()
        else:
            print("Esse são os clientes na fila de espera: ")
            for i, cliente in enumerate(lista_de_espera,start=1):
                print(f"posição na lista {i} nome : {cliente}")
            print()
tamanho_da_lista_restante = len(lista_de_espera)
print()
print("FECHANDO RESTAURANTE...")
if tamanho_da_lista_restante > 0 :
    for cliente in lista_de_espera:
        print(f"- {cliente}")
print(f"A quantidade de atendimentos foi: {contador_de_chamados}")