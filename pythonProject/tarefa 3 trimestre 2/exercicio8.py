def divisivelPorDois(numero):
    if numero % 2 == 0:
        print(f"o numero{numero} pode ser divisivel por 2")
    else:
        print(f"o numero {numero} não pode ser divisivel por 2")

def divisivelPorTres(numero):
    if numero % 3 == 0:
        print(f"O numero {numero} pode ser divisivel por 3")
    else:
        print(f"o numero {numero} não pode ser divisivel por 3")



numero = int(input("Digite um numero: "))

divisivelPorDois(numero)
divisivelPorTres(numero)
