# Usando a função open para criar um objeto do tipo arquivo
arquivo = open("c:\\arquivos\\arquivo.txt", "r", encoding="UTF-8")

# Verificando o tipo  do arquivo
print(type(arquivo))

print("")

# Printando o arquivo
print(arquivo)


#Printando o conteúdo do objeto arquivo
#print(arquivo.read())

#Printando uma linha do arquivo
#   print(arquivo.readline())

#Printando outra linha do arquivo
#   print(arquivo.readline())

#Passando o conteúdo do arquivo para uma lista
lista_linhas = arquivo.readlines()

#Comprovando o tipo do objeto texto
print(type(lista_linhas))
print(lista_linhas)

#Colocando a linha em ordem alfabética
lista_linhas.sort()
print(lista_linhas)

#Exibindo uma linha por vez, utilizando for
for linha in lista_linhas:
    print(linha)

#Fechando o arquivo
arquivo.close()