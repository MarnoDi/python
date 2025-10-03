def verificacaoDeParOuImpar(numero):
    if numero % 2 != 0:
        print(f"O número {numero} é PAR")
    else:
        print(f"O número {numero} é ÍMPAR")

numero = int(input("Digite um numero: "))

verificacaoDeParOuImpar(numero)