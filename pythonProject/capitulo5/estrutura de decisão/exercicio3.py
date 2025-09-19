def maiorNumero(numero1, numero2, numero3):
    if (numero1 >= numero2 >= numero3):
        print("o", numero1, "é  maior")
        if (numero2 >= numero3 >= numero1):
            print("o", numero2, "é maior")
            if (numero3 >= numero2 >= numero1):
                print("o", numero3, "é maior")


numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))
numero3 = int(input("Digite o terceiro numero: "))

maiorNumero(numero1, numero2, numero3)
