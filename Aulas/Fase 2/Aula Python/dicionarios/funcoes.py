#Formas de exibir o dicionário em Python

#Criação do  dicionário
dicionario = {
   "Yoda": "Mestre Jedi",
    "Obi-Wan": "Mestre Jedi",
   "Anakin": "Cavaleiro Jedi",
    "R2-D2": "Dróide",
    "Dex": "Balconista"
}

#Maneira convencional
print(f"{dicionario}\n")

#Exibindo o valor de uma chave conhecida
print(f"{dicionario['Yoda']}\n")

#Usando o metodo get // Melhor que o anterior pois caso insira uma chave inexistente ele informa none e não da erro no código
print(dicionario.get("Dex"))

#Matodo para retornar uma lista com as chaves  do dic
print(dicionario.keys())

for chave in dicionario.keys():
    print(dicionario[chave])

#Metodo para retornar uma lista com os valores
print(dicionario.values())

print(len(dicionario.values()))
print("Mestre Jedi" in dicionario.values())
print("Sith" in dicionario.values())

#Retorna tuplas com (chave,valor)
print(dicionario.items())

#Desempacotando dicionarios
for nome, categoria in dicionario.items():
    print(f"O personagem {nome} é um {categoria}")

#Inserção de Valores
dicionario.update({"Andre":"Professor"})
for nome, categoria in dicionario.items():
    print(f"O personagem {nome} é um {categoria}")