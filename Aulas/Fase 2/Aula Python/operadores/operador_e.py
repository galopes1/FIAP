#Para acessar um sistema, o usuário deve digitar o username darth_vader e a senha 1138
#Crie um script que receba e valide estas informações de acesso

username = input("Digite o seu nome de usuário: ")
senha = input("Digite sua senha: ")

if username.lower() == "darth_vader" and senha == "1138":
    print("Login realizado com sucesso!")
else:
    print("Falha no login! Senha ou username incorretos!")