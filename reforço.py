opcao_escolhida = -1
lista_alunos = []
lista_medias = []
contador_de_aprovados = 0
contador_de_reprovados = 0
def  nota_valida(mensagem):
    while True:
        try:
            nota = float(input(mensagem)) # recebe a nota 
            if 0 <= nota <= 10 : # desvio condicional para checar se a nota está entre 0 e 10
                return nota # caso passe do desvio ele retorna o valor 
            else:
                print("ERRO: insira uma nota entre 0 à 10 por favor") # Caso contrário
        except ValueError:
            print("VALOR INSERIDO NÃO É ACEITO (ex: 8.5, 4.5 3.8 ...)")# Caso específico de inserir um tipo diferente de float


while True:
    print("Opção 1 cadastrar um novo aluno com suas 3 notas")
    print("Opção 2 mostrar a lista de todos os alunos com suas médias e situação")
    print("Opção 3 remover um aluno pelo nome")
    print("Opção 4 mostrar um relatório final da turma")
    print("Opção 5 sair do sistema (digite 'sair')")
    opcao_escolhida = input("O que você deseja fazer ? ").lower()
    if opcao_escolhida == "sair" or opcao_escolhida == "5":
        print("Encerrando ...")
        break
    # Desvios condicionais/ opções 
    elif opcao_escolhida == "1":
        nome_aluno = input("Digite o nome do aluno ").lower()
        if nome_aluno in lista_alunos: # checa o nome na lista 
            print(f"O aluno {nome_aluno} já está cadastrado !") # se já existir
        else:
            lista_alunos.append(nome_aluno) # Caso não exista 
            print("--- NOTAS ---")
            nota1 = nota_valida("Insira a nota 1°: ")
            nota2 = nota_valida("Insira a nota 2°: ")
            nota3 = nota_valida("Insira a nota 3°: ")
            soma = (nota1 + nota2 + nota3) / 3
            lista_medias.append(soma)
    
    #Opção 2 - Lista inteira com alunos, notas e situação
    elif opcao_escolhida == "2":
        if len(lista_medias) >  0:
            for i, aluno in enumerate(lista_alunos, start=1) : # Pega a lista de alunos e muda no print o indice inicial para 1
                media_aluno = lista_medias[i - 1] # Porém aqui a ele pega o i e subtrai por 1 para achar o verdadeiro índice 
                if media_aluno >= 6 : # Desvio básico para checar a situação do aluno 
                    situação = "APROVADO"
                else:
                    situação = "Não posso fazer nada, aluno "
                print(f"O Aluno {aluno} está {situação} | média: {media_aluno}")
                print()
        else:
            print("NÃO TEM NINGUÉM NA LISTA AINDA ")
            print()
    # Opção para remover o aluno e sua média também 
    elif opcao_escolhida == "3":
        if len(lista_medias) >  0:
            nome_aluno = input("Digite o nome do aluno ")
            if nome_aluno in lista_alunos:
                #prcesso para remover tanto o aluno quanto sua média para impedri bugs de ordem das notas !!!
                posicao = lista_alunos.index(nome_aluno) # transforma o valor inserido no input em um índice 
                del lista_alunos[posicao] # remove ele na lista de alunos
                del lista_medias[posicao]# e também na lista de médias 
            else:
                print("Esse aluno não esta presente na lista ")
        else:
            print("NÃO TEM NINGUÉM NA LISTA AINDA ")
            print()
    elif opcao_escolhida == "4":
        if len(lista_medias) >  0: # teste rápido pra verificar se tem um iterável na lista 
            for i, aluno in enumerate(lista_alunos, start=1):
                media_aluno = lista_medias[i - 1]
                if media_aluno >= 6:
                    contador_de_aprovados += 1
                else:
                    contador_de_reprovados += 1
            print("--- Melhores/Piores Notas ---")
            #Para pegar a melhor nota e seu indice de acordo com o dono da nota 
           
            melhor_nota = max(lista_medias) # Pegamos a melhor nota com "max" e atribuimos para a variável
            posicao_melhor = lista_medias.index(melhor_nota) # pegamos a posição do melhor à partir da nota
            melhor_aluno = lista_alunos[posicao_melhor] # vinculamos a melhor nota à lista de alunos por estarem vinculadas
            
            #Mesma coisa só que dessa vez para a pior nota 
            
            pior_nota = min(lista_medias)
            posicao_pior = lista_medias.index(pior_nota)
            pior_aluno = lista_alunos[posicao_pior] 
            print("--- RELATÓRIO GERAL ---  ")
            
            #Cálculo para pegar a media geral da classe ...

            media_geral = sum(lista_medias) / len(lista_alunos)
            
            print(f"As media geral foi de {int(media_geral)}... ")
            print(f"A melhor nota foi {int(melhor_nota)} de {melhor_aluno}")
            print(f"A pior nota foi de {int(pior_nota)} de {pior_aluno}...")
            print(f"A quantidade de aprovados foram {contador_de_aprovados} ")
            print(f"A quantidade de alunos repovados foram {contador_de_reprovados}")
        else: 
            print("NÃO TEM NINGUÉM NA LISTA AINDA ")
            print()