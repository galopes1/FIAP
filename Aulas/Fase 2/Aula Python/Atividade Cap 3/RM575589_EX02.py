preco = float(input("Digite o preço do carro: "))

preco_vista = preco * 0.8
print(f"O preço final á vista com desconto de 20% é : R${preco_vista:.2f}")

# Considerei que como o percentual começa em 3% e aumenta mais 3% a cada 6 meses irei usar no loop
percentual = 0.03

# Laço de repetição que vai de 6 até 60, andando de 6 em 6
for parcelas in range(6, 61, 6):
    preco_final = preco * (1 + percentual)
    valor_parcela = preco_final / parcelas

    print(f"O preço final parcelado em {parcelas} X é de R${preco_final:.2f} com parcelas de R${valor_parcela:.2f}")

    percentual += 0.03
