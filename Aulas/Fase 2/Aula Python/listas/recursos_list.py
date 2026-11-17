#valores fora de ordem
valores = [1, 7, 7, 19, 3, 2, 11, 15, 6, 1, 5, 3.5]

#exibição da lista
print(f"A lista foi criada assim: {valores}")

#contagem de elementos 1
contagem = valores.count(1)
print(f"A contagem de números 1 foi de {contagem}")


#Invertendo a lista
valores.reverse()
print(f"A lista invertida ficou assim: {valores}")

#Ordenando a lista
valores.sort()
print(f"A lista ordenada ficou assim: {valores}")

valores.sort(reverse=True)
print(f"A lista em ordem descrescente ficou assim: {valores}")

#Tamanho da lista
tamanho = len(valores)
print(f"A quantidade de elementos na lista é {tamanho}")


#Soma dos elementos
soma = sum(valores)
print(f"A soma dos valores é {soma}")