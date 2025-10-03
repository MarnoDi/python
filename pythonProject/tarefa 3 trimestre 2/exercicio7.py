def verificadorDeNumeroSeForZero(numero):
    if numero == 0:
        print("É zero!")
    elif numero > 0:
        print(f"O numero {numero} é positivo")
    else:
        print(f"o numero {numero} é negativo")


numero = float(input("Digite um numero: "))

verificadorDeNumeroSeForZero(numero)