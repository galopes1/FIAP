#Criação e exibição da tupla
tupla = (1, 7, 7, 19, 3, 2, 11, 15, 6, 1, 5)
print(f"A tupla criada ficou assim: {tupla}")

#Utilizando enumerate para mostrar uma sequência // Funciona em tuplas com int e str
for numero, valor in enumerate(tupla):
    print(f"No índice {numero} temos: {valor}")

#Mostrando a quantidade de itens na tupla // Funciona em tuplas com int e str
print(f"Quantidade: {len(tupla)}")

#Mostrando o menor valor na tupla // A tupla precisa ter obrigatoriamente apenas valores númericos
print(f"Menor valor: {min(tupla)}")

#Mostrando o maior valor da tupla // A tupla precisa ter obrigatoriamente apenas valores númericos
print(f"Maior valor: {max(tupla)}")

#Mostrando a soma de todos os valores da tupla // A tupla precisa ter obrigatoriamente apenas valores númericos
print(f"Soma dos valores: {sum(tupla)}")

#utilizando tuple() para a conversão de uma lista para uma tupla
lista = [True, False]
print(f"Lista: {lista}")
tupla2 = tuple(lista)
print(f"Tupla: {tupla2}")

#Criando a tupla3 com os valores 1 (true) e 0 (false)
tupla3 = (1,0)

#função all
print(f"Testando a tupla2 com all:  {all(tupla2)}")
print(f"Testando a tupla2 com all:  {all(tupla3)}")

#função any
print(f"Testando a tupla2 com any:  {any(tupla2)}")
print(f"Testando a tupla2 com any:  {any(tupla3)}")

