print("Promoção da Vivo! \nDigite seu número de pontos abaixo!")
num = int(input("-> "))

if num >= 1000:
    print("Parabéns! Você tem 3gb de bônus!")
elif num >= 500:
    print("Parabens! Você tem 1,5gb de bônus!")
elif num >= 200:
    print("Parabéns! Você tem 500mb de bônus!")
else:
    print("Você não tem pontuação suficiente para receber bônus.")