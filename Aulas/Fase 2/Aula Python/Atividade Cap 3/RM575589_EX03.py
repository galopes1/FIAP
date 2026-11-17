# Recebendo o valor da divida
valor_divida = float(input("Digite o valor da divida: "))

# Iniciando variaveis para meu laço sendo juros = 1 para a conta do valor total com o juros e começando com 1 parcela
juros = float(1)
parcelas = 1

# Laço com 5 exibições conforme exemplo
for i in range(1, 6):
    total = valor_divida * juros
    valor_juros = total - valor_divida
    valor_parcela = total / parcelas
    print(f"Total: R${total:.2f} Juros: R${valor_juros:.2f} Número de parcelas: {parcelas} Valor da Parcela: {valor_parcela:.2f}")

#Como da primeira parcela/% de juros para a segunda muda +2/+10% e o resto mantém um padrão de +3/+5% tratei o primeiro caso e padronizei o resto
    if juros == 1:
        juros += 0.1
    else:
        juros += 0.05

    if parcelas == 1:
        parcelas += 2
    else:
        parcelas += 3