categorias = ("A", "B", "C", "D", "E")

categoria = input("Insira a categoria da sua CNH: ")

if categoria in categorias:
    print("Categoria existente!")
else:
    print("Categoria inexistente!")