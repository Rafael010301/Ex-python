print("--- BANCO RADESCO ---")
nome = input("Insira seu nome : ")
capital = float(input("Digite seu saldo inicial : "))
valor_saque = float(input("Digite seu valor de saque : "))
contador_de_saldos = 0
soma_de_saque = 0
if valor_saque <= capital:
    if valor_saque <= 0 : # Para evitar um saque negativo 
        print("Valor de saque negativo !")
    else:
        while valor_saque != 0:# condição inicial para sair do ou entrar no loop
            contador_de_saldos += 1
            soma_de_saque += valor_saque
            capital -= valor_saque
            valor_saque =  float(input("Digite seu valor de saque : "))
            if valor_saque > capital : # Caso eu peça mais do que eu tenha dentro do loop
                break
        print("Dados atuais : \n ", # Resultado caso eu digite 0 e saia do loop
            "Nome:", nome,"\n",
            "Saldo Final:" ,capital,"\n",
            "Quantidade de vezes que houve um saque",contador_de_saldos,"\n",
            "Quantia de saques : ",soma_de_saque)
else: # Umas das condições inicias caso eu logo de cara peça mais do que eu tenha 
    print()
    print("Saldo insuficente !!!")
    print()
    print("Dados atuais:")
    print("Nome : ",nome ,"\n","Saldo Final: ", capital, "\n","Quantidade de vezes que houve um saque: ",contador_de_saldos,"\n","Quantia sacada: ",soma_de_saque)
    