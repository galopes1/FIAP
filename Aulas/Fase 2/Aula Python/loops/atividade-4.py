minutos = int(input("Digite os minutos atuais: "))
conta = minutos
for i in range(1, minutos):
    conta =  conta * i

print(conta)

conta = str(conta)

senha = "LIBERDADE"
senhafinal = senha + conta

senha_digitada = input("Digite a senha: ")
if senha_digitada == senhafinal:
    print("Senha valida!")

else:
    print("Senha invalida!")
