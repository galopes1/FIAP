# Uma universidade realizará uma competição acadêmica. Para essa competição, só serão aceitos estudantes que sejam maiores de idade.
#Crie um programa que receba o RM e a idade de um aluno, e exiba uma mensagem confirmando o cadastro apenas caso o estudante seja de maior

#inicio do programa
print("Competição acadêmica!!")
rm = input("Digite seu RM: ")
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print(f"Cadastro do RM:{rm} foi realizado com sucesso!")
else:
    perm = input("Você possui autorização dos responsáveis para participar? S - Sim ou N - Não \n")
    if perm == "S":
        print(f"Cadastro do RM:{rm} foi realizado com sucesso!")
    else:
        print(f"Cadastro do RM:{rm} foi negado pois o aluno é menor de idade.")



print("Os detalhes serão enviados para o seu email!")

