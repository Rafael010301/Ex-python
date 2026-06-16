validação_de_jogo = input("Você quer jogar ? ").lower()
pontos_partida = 0
pontos_especiais = 0
contador_de_partidas = 0
while validação_de_jogo == "sim":
    for resposta in range(1,6):
        print(f"{resposta}° partida ! ")
        pergunta = int(input("Quantos é 7 * 9 ? "))# 1° pergunta 
        if pergunta == 63:
            print("CORRETO !")
            pontos_partida += 20
            pontos_especiais += 1
        else:
            print("ERRADO ! A resposta é 63 ")
            pontos_especiais -= 1
        pergunta = int(input("Qual o resultado da multiplicação 8 * 7 "))# 2° pergunta
        if pergunta == 56:
            print("CORRETO ! Mais um ponto para você !!!")
            pontos_partida += 20
            pontos_especiais += 1
        pergunta = int(input("Qual é a raiz quadrada de 121 ? "))# 3° pergunta
        if pergunta == 11:
            print("CORRETO! parabéns ! mais um ponto !!")
            pontos_partida += 20
            pontos_especiais += 1
        else:
            print("ERRADO ! a resposta correta é 11 !")
            pontos_especiais -= 1
        pergunta = int(input("Qual o resultado da operação: 200 + 300 / 2 ? "))# 4°  pergunta
        if pergunta == 350:
            print("CORRETO !!! está indo bem !! mais um pontos para você ")
            pontos_partida += 20
            pontos_especiais += 1
        else:
            print("ERRADO ! A resposta é 350 ! ")
            pontos_especiais -= 1
        pergunta = int(input("Qual o resultado dessa operação ? (235 + 300) * (300 - 200) "))
        if pergunta == 53500:
            print("PARABÉNS VOCÊ ACERTOU A ÚLTIMA PERGUNTA !!")
            pontos_partida += 20 
            pontos_especiais += 1
        #repetição da partida
        validação_de_jogo = input("Você quer jogar de novo ? ").lower()
        if validação_de_jogo != "sim":
            break
        else:
            contador_de_partidas += 1
    print("============")
    print("FIM DE JOGO \n")
    print(f"Pontos totais: {pontos_partida}")
    print(f"pontos especiais : {pontos_especiais}")
        
print("=== FIM DE JOGO ===")