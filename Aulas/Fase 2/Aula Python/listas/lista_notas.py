
notas = []

while input("Deseja inserir uma nota? S - Sim, N - Não\nR: ").upper() != "N":
    notas.append(float(input("Por favor, insira a nota: ")))


media = sum(notas) / len(notas)

print(f"A soma das notas foi de : {sum(notas):.2f}\nA média das notas foi de : {media:.2f}")