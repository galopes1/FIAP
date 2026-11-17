#variavel para armazenar o peso total das caixas
peso_total = 0.0
#loop para repetir por 100 vezes a solicitação de peso
for x in range(1,101):
    #para cada volta do loop, solicitar o peso da caixa
    peso_atual = float(input(f"Informe o peso da {x}ªcaixa: "))
    #para cada peso solicitado, somar ao peso total
    peso_total = peso_total + peso_atual
#ao final do loop, calcular a média aritmética
media = peso_total/100
#exibição dos resultados!
print("O peso total de caixas é {}. \nA média de peso é {}".format(peso_total, media))