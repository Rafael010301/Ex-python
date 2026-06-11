equipe_tamanho = int(input("Digite o tamanho de sua equipe: "))
dias_analisados = int(input("Digite os dias para serem analisados: "))
maior_venda = 0
soma_das_vendas = 0
media_das_vendas = 0
maior_total = 0
melhor_do_dia =0

for vendedor in range(equipe_tamanho):
    nome = input("Digite seu seu nome ")

    folgas = 0
    total_vendedores = 0
    for dia in range(dias_analisados):
        venda = int(input("Quanto você vendeu no dia " + str(dia + 1) + " : "))

        total_vendedores = total_vendedores + venda
        media_vendas = total_vendedores/dias_analisados

        if venda == 0:
            folgas = folgas + 1
            continue
        if melhor_do_dia > total_vendedores:
            total_vendedores = melhor_do_dia
            nome = total_vendedores
    
    soma_das_vendas = soma_das_vendas + total_vendedores 
    
    print(nome + " Vendeu no total "+ str(total_vendedores) + " com uma média de "+ str(media_vendas)+ " com " + str(folgas) + " dias de folga")
if maior_total > total_vendedores:
    total_vendedores = maior_total
    nome = total_vendedores
print()
print("--- Resultado relatório --- \n")
print()
print("Total de vendas foi: ", soma_das_vendas,"\n")
print(f"o Melhor funcionário foi {nome}")