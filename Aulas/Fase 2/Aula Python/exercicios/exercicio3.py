ps = 0
xs = 0
ns = 0

for i in range(5):
    escolha = input(f"Colaborador {i+1} escolha: PlayStation, Xbox ou Nintendo: ")
    if escolha.lower() == "playstation":
        ps = ps + 1
    elif escolha.lower() == "xbox":
        xs = xs + 1
    elif escolha.lower() == "nintendo":
        ns = ns + 1

escolhido = ps
console = "PlayStation"
if escolhido < xs:
    escolhido = xs
    console = "Xbox"
elif escolhido < ns:
    escolhido = ns
    console = "Nintendo"

print(f"O console escolhido foi o {console}")
