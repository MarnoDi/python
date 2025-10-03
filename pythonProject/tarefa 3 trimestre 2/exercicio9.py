def divisivelPorCincoOuTres(numero):
    if numero % 5 == 0 or numero % 3 == 0:
        print(f"o numero {numero} pode ser divisivel por 5")
        print(f"o numero {numero} pode ser divisivel por 3")
    else:
        print(f"o numero {numero} não pode ser divisivel por 5")
        print(f"o numero {numero} não pode ser divisivel por 3")



numero = int(input("Digite um numero: "))

divisivelPorCincoOuTres(numero)
