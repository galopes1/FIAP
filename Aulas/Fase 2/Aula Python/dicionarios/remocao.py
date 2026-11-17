dicionario = {
    "Yoda": "Mestre Jedi",
    "Mace Windu": "Mestre Jedi",
    "Anakin Skywalker": "Cavaleiro Jedi",
    "R2-D2": "Dróide",
    "Dex": "Balconista"
}

print(dicionario)

#Remoção com .pop // Remove a chave e valor

dicionario.pop("Yoda")
print(dicionario)

#Remoção com .popItem() // Remove o último item
dicionario.popitem()
print(dicionario)

#Remover todos os elementos do dicionario
dicionario.clear()
print(dicionario)