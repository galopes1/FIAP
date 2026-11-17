#código sem função

#distancia = float(input("Digite a distância percorrida: "))
#tempo = float(input("Digite o tempo da viagem: "))

#velocidade_m = distancia / tempo

#print(f"A velocidade média é {velocidade_m:.2f} km/h")

def calcularVelocidadeMedia():
    distancia = float(input("Digite a distância percorrida: "))
    tempo = float(input("Digite o tempo da viagem: "))

    velocidade_m = distancia / tempo

    print(f"A velocidade média é {velocidade_m:.2f} km/h")

calcularVelocidadeMedia()

#É a mesma coisa do código, porém você pode reutiliza-lo quantas vezes quiser ao decorrer do código