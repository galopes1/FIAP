#importando o módulo json
import json

#usando a função open para criar um objeto do tipo arquivo
arquivo = open("C:\\arquivos\\agenda.json", "r", encoding="UTF-8")

#Colocando o conteúdo do arquivo em uma variável do tipo String
dicionario = json.loads(arquivo.read())

#Fechando o arquivo
arquivo.close()


# Usando o metodo loads para converter uma string no formato json em um dicionário
print(dicionario)