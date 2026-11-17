print("Escolha o tipo de investimento: \n1.CDB\n2.LCI\n3.LCA")

# Laço while para o caso do usuario digitar um tipo de investimento inválido, repetindo até ele digitar corretamente (1, 2, 3)
retorno = 1
while retorno == 1:
    tipo_inves = int(input("Digite o tipo de investimento (1,2 ou 3): " ))
    if tipo_inves != 1 and tipo_inves != 2 and tipo_inves != 3:
        print("Digite um tipo de investimento existente!")
        retorno = 1
    else:
        retorno = 0

# Entrada dos valores de dia e valor
valor_resgate = float(input("Digite o valor a ser resgatado: "))
dias = int(input("Digite o número de dias que o valor permaneceu investido: "))

# Cálculo dos juros baseado nos dias, conforme a tabela da aliquota
if tipo_inves == 2 or tipo_inves == 3:
    print("O seu tipo de investimento é livre de imposto de renda.")
elif tipo_inves == 1:
    if dias <= 180:
        aliquota = 0.225
    elif dias <= 360:
        aliquota = 0.20
    elif dias <= 720:
        aliquota = 0.175
    elif dias > 720:
        aliquota = 0.15

# Cálculo do valor final e imprime a mensagem monstrando-o
    valor_juros = aliquota * valor_resgate
    print(F"O valor do imposto de renda a ser pago é: R$ {valor_juros:.2f}")




