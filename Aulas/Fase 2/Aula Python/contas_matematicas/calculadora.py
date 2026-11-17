print("Calculadora!")
x = "sim"

while x in ["sim","Sim","s","S"]:
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo numero: "))

    operacao = input("Digite a operação desejada:\n +(adição), -(subtração), /(divisão e *(multiplicação)\n")

    match operacao:
        case "adição" | "+":
            soma = num1 + num2
            print(f"A soma é {soma}")
        case "subtração" | "-":
            sub = num1 - num2
            print(f"A subtração é {sub}")
        case "divisão" | "/":
            div = num1 / num2
            print(f"A divisão é {div}")
        case "*" | "multiplicação":
            mult = num1 * num2
            print(f"A multiplicação é {mult}")
    x = input("Deseja fazer outra operação? Sim ou não\n")
