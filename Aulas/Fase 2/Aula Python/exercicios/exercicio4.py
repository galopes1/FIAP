nivel = input("Digite seu tipo de assinatura: ")
fat_anual = float(input("Digite o valor do seu faturamento anual: "))

if nivel.lower() == "basic":
    bonus = fat_anual * 0.30
elif nivel.lower() == "silver":
    bonus = fat_anual * 0.20
elif nivel.lower() == "gold":
    bonus = fat_anual * 0.10
elif nivel.lower() == "platinum":
    bonus = fat_anual * 0.05

print(f"O valor do bônus será de R${bonus:.2f}")