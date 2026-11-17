contatos = {
    "Clark Kent":
        {"Celular": "123456",
        "Email:":"super@krypton.com"},
    "Bruce Wayne":
        {"Celular":"654352",
          "Email:":"bat@caverna.com.br"}
}

for nome, contato in contatos.items():
    print(f"{nome}")
    for tipo, contato in contato.items():
        print(f"{tipo}: - {contato}")
    print("--------------")