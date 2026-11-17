bruto_pacote = float(input("Digite o valor bruto do pacote: "))
categoria_ass = input("Digite a categoria do assento: ")
qnt_pessoas = int(input("Digite a quantidade de pessoas: "))

if categoria_ass.lower() == "econômica":
    if qnt_pessoas == 2:
        desconto = 0.03
    elif qnt_pessoas == 3:
        desconto = 0.04
    elif qnt_pessoas >= 4:
        desconto = 0.05
elif categoria_ass.lower() == "executiva":
    if qnt_pessoas == 2:
        desconto = 0.05
    elif qnt_pessoas == 3:
        desconto = 0.07
    elif qnt_pessoas >= 4:
        desconto = 0.10
elif categoria_ass.lower() == "primeira classe":
    if qnt_pessoas == 2:
        desconto = 0.10
    elif qnt_pessoas == 3:
        desconto = 0.15
    elif qnt_pessoas >= 4:
        desconto = 0.20

valor_desconto = desconto * bruto_pacote
valor_liquido = bruto_pacote - valor_desconto
media = valor_liquido / qnt_pessoas

print(f"Bruto da viagem: R${bruto_pacote:.2f}\n Valor do desconto: R${valor_desconto:.2f}\n Valor liquido: R${valor_liquido:.2f}\n Valor médio por viajante: R${media:.2f}")
