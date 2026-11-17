#Importando classe Math

import math

#Solicitando os valores de A,B e C

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))
c = float(input("Digite o valor de C: "))

#Cálculo do Delta e Baskara

delta = b * b - 4 * a * c

if delta > 0.0:

    x1 = (-b + math.sqrt(delta)) / (2 * a)
    x2 = (-b - math.sqrt(delta)) / (2 * a)
    print(f"Para a equação {a}x² + {b}x + {c} obtivemos os seguintes valores: x1= {x1} e x2= {x2}")
elif delta == 0:

    x = (-b + math.sqrt(delta)) / (2 * a)
    print(f"Para a equação {a}x² + {b}x + {c} obtivemos o seguinte valor: x= {x}")

else:
    print("Não existem valores reais para essa equação.")