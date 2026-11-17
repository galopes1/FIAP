bpm = int(input("Informe o seu número de BATIMENTOS POR MINUTO: "))
idade = int(input("Informe a sua idade: "))

if idade <= 2:
    if bpm >= 120 and bpm <= 140:
        print("Batimentos dentro da faixa adequada até 2 anos!")
    else:
        print("Batimentos fora da faixa adequada!")
elif idade >= 8 and idade <=17:
    if bpm >= 80 and bpm <= 100:
        print("Batimentos dentro da faixa adequada de 8 até 17 anos!")
    else:
        print("Batimentos fora da faixa adequada!")
elif idade >= 65:
    if bpm >= 50 and bpm <= 60:
        print("Batimentos dentro da faixa adequada para idosos!")
    else:
        print("Batimentos fora da faixa adequada!")
elif idade > 18 and idade < 65:
    if bpm >= 70 and bpm <= 80:
        print("Batimentos de um adulto sedentário!")
    elif bpm <= 66:
        print("Batimentos dentro da faixa adequada!")
    else:
        print("Batimentos fora da faixa adequada!")

