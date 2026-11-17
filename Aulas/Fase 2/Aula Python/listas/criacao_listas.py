#Criação de uma lista vazia
jedi = []
print(type(jedi))

#Criação de uma lista com os Jedi Yoda, Luke, Obi-Wan, Anakin
jedi = ["Yoda", "Luke", "Obi-Wan","Anakin"]

#Exibição de uma lista completa
print (jedi)

#Exibição de uma posição específica na lista
print(jedi[1])

#Exibição dos últimos elementos
print(jedi[-1])
print(jedi[1:3])

for nome in jedi:
    print(nome)

#Inserção no fim da lista
jedi.append("Luminara")
print(jedi)

#Inserção no fim da lista com input
jedi.append(input("Insira o nome de um Jedi: "))
print(jedi)

#Inserção em uma posição exata
jedi.insert(1,"Cebolinha")
print(jedi)

# .append insere um valor no fim da lista// .insert adiciona em uma posição especifica e "empurra" as demais para frente
