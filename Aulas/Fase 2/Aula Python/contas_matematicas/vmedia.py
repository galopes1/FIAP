#Nome do programa
print("Cálculo da velocidade média ")

#Solicitando a distância do percurso
distancia = float(input("Digite a distância percorrida em quilometros: "))

#Solicitando o tempo do percurso
tempo = float(input("Digite o tempo do percurso em horas: "))

#Cálculo da velocidade média
velocidade_media = distancia / tempo

#Exibição do calculo
print(f"O patinete atingiu uma velocidade de {velocidade_media:.1f} km/h")