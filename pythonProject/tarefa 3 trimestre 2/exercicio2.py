def leitorNumero(numero):
    resultado = numero ** 2
    if (resultado > 0):
        print("o resultado deu", resultado, "logo, é maior é zero")
    else:
        print("é menor que zero")
        if (resultado < 0):
            print("o restultado deu", resultado, "logo, é negativo")


numero = int(input("Põe um numero ae: "))

leitorNumero(numero)