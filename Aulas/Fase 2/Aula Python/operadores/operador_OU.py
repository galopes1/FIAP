
valor_compra = float(input("Digite o valor do compra: "))
cupom = input("Digite um cupom válido: ")
if cupom.lower() == "festa" or valor_compra >= 1000:
    valor_compra = valor_compra * 0.9

input(f"O valor da compra é R${valor_compra:.2f}")
