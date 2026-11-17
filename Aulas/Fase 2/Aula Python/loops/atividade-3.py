print("Bem vindo ao desafio da sorte Fibonacci")

numero_us = int(input("Por favor, informe um número inteiro: "))

anterior = 0
atual = 1

for i in range(1, numero_us + 1,1):
    proximo = anterior + atual
    atual = anterior
    anterior = proximo
    if numero_us == proximo:
        print("Ação bem sucedida!")
        break
    elif numero_us < proximo:
        print("Ação falhou")
        break
