#Texto de introdução da pesquisa
print("Fintech Bidu - Pesquisa de realização mentoria financeira")

#criação das variáveis dos dias
segunda = 0
terca = 0
quarta = 0
quinta = 0
sexta = 0


#entrada do número de colaboradores que irão participar
num_colab = int(input("Informe o número de colaboradores: "))

#loop baseado no valor de colaboradores
for i in range(num_colab):
    #entrada da opção escolhida
    dia = input("Informe o dia da sua preferência (segunda-feira, terça-feira, quarta-feira, quinta-feira, sexta-feira) \nR: ").lower()

#adicionando +1 na variável do dia escolhido
    if dia == "segunda-feira" or dia == "segunda feira":
        segunda += 1
    elif dia == "terça-feira" or dia == "terça feira" or dia == "terca feira" or dia == "terca-feira":
        terca += 1
    elif dia == "quarta-feira" or dia == "quarta feira":
        quarta += 1
    elif dia == "quinta-feira" or dia == "quinta feira":
        quinta += 1
    elif dia == "sexta-feira" or dia == "sexta feira":
        sexta += 1

#comparando qual dia foi o mais escolhido / iniciando assumindo que a segunda é a vencedora e comparando um a um após

vencedor = segunda
dia_vencedor = "segunda-feira"

if vencedor < terca:
    vencedor = terca
    dia_vencedor = "terça-feira"
if vencedor < quarta:
    vencedor = quarta
    dia_vencedor = "quarta-feira"
if vencedor < quinta:
    vencedor = quinta
    dia_vencedor = "quinta-feira"
if vencedor < sexta:
    vencedor = sexta
    dia_vencedor = "sexta-feira"

#verificando possibilidade de empate
empates = 0
if segunda == vencedor:
    empates += 1
if terca == vencedor:
    empates += 1
if quarta == vencedor:
    empates += 1
if quinta == vencedor:
    empates += 1
if sexta == vencedor:
    empates += 1


if empates > 1:
    print("O dia escolhido pelos colaboradores resultou em empate e será realizada uma nova votação.")
else:
    print(f"O dia escolhido pelos colaboradores é: {dia_vencedor}")

