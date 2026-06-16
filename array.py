sabores_pizza = ["pepperoni", "mussarela", "calabresa","4 queijos"]
votos_sabores = [0,0,0,0]
soma_de_votos = 0
votos_invalidos = 0
votos_validos = 0
print("======= M E N U ========= ")
while True:
    for indice, sabor in enumerate(sabores_pizza, start= 1):
        print(f"Esses são os sabores {indice}:  - {sabor}  ")
    print(" Pressione 0 para sair ")
    voto = int(input(" Escolha um dos valores, ou digite 0 para sair: "))
    if voto == 0 :
        break
    elif voto >= 1 and voto <= 4:
        posicao = voto - 1
        votos_sabores[posicao] += 1
        votos_validos += 1 
        print(f"VOTO VALIDADO EM {sabores_pizza[posicao]}")
    else:
        print("VOTO INVÁLIDO")
        votos_invalidos += 1
    
    
print("--- Fase de apuração ---")
for i in range(len(votos_sabores)): 
    print(f"votos totais de {sabores_pizza[i]} {votos_sabores[i]}")
print(f" votos no total (válidos): {votos_validos}")
print(f"votos inválidos: {votos_invalidos}")

    
    