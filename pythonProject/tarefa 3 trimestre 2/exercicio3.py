def maiorNumero(numero1, numero2, numero3):
    if(numero1 > numero2):
        if(numero1 > numero3):
            print("o primeiro numero é o maior")
    elif (numero2 > numero3):
        print("o segundo numero é o maior")
    else:
        print("o terceiro numero é o maior")


numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))
numero3 = int(input("Digite o terceiro numero: "))

maiorNumero(numero1, numero2, numero3)
