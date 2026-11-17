email = input("Digite seu e-mail: ")
nota = float(input("Digite sua nota média: "))

if nota >= 8.5:
    print(f"ENVIANDO E-MAIL PARA {email}")
else:
    print("Programa encerrado")
