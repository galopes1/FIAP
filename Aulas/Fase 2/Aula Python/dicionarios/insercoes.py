funcionarios = {}

while input("Deseja inserir um novo funcionário? S-Sim, N-Não\nR:").upper() != "N":
    nome = input("Digite o nome do funcionário: ")
    funcao = input("Digite a função do funcionário: ")
    funcionarios.update({nome: funcao})

print(funcionarios)