#importando o módulo json
import json

#Criando um dicionário para usarmos como exemplo
contatos = {

    "Clark Kenté":
        {"Celular": "123456",
         "Email":"super@krypton.com"},
    "Bruce Wayne":
        {"Celular": "123456",
         "Email":"bat@caverna.com"}

}

# Convertendo o dicionário para uma string o formato json
conteudo_string = json.dumps(contatos, indent=4, ensure_ascii=False)

#Criando um arquivo
arquivo = open("C:\\arquivos\\agenda.json", "w", encoding="UTF-8")

#Escrevendo o JSON dentro do arquivo
arquivo.write(conteudo_string)

#Fechando o arquivo
arquivo.close()