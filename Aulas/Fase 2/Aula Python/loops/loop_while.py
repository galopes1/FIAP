resposta = ""
tentativas = 0

while resposta != "42":
    resposta = input("Qual a resposta para a vida, o universo e tudo mais? \n")
    tentativas = tentativas + 1

print(f"Parabéns, você acertou! Após {tentativas} tentativas!")

i = 1
while i <= 10:
    print(f"Mais uma mengasem, com i valendo {i}")
    i = i + 1
