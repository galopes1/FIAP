numt = int(input("Digite quantas transações financeiras você realizou ao longo do dia: "))
total = 0

for i in range(1, numt+1):
    valor = int(input(f"Digite o valor da {i}ª transação: "))
    total = total + valor

media = total / numt
print(f"Você gastou R${total:.2f} e a média por transação foi de R${media:.2f} reais")