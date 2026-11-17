alimentos = int(input("Informe quantos alimentos consumiu no dia: "))
total_calorias = 0

for i in range(1,alimentos + 1):
    num = int(input(f"Informe o número de calorias do {i}º alimento: "))
    total_calorias = total_calorias + num

print(f"Você consumiu {total_calorias} calorias no dia informado.")