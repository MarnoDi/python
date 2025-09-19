def calculaMedia(numero1, numero2, numero3, numero4):
    quantidadePar = 0
    totalPares = 0

    if(numero1 % 2 == 0):
        quantidadePar += 1
        totalPares += numero1
        if (numero2 % 2 == 0):
            totalPares += numero2

            if (numero3 % 2 == 0):
                totalPares += numero3

                if (numero4 % 2 == 0):
                    totalPares += numero4

                    return quantidadePar



numero1 = int(input("Digite o primeiro numero: "))
numero2 = int(input("Digite o segundo numero: "))
numero3 = int(input("Digite o terceiro numero: "))
numero4 = int(input("Digite o quarto numero: "))

totalMedia = calculaMedia(numero1, numero2, numero3, numero4)


print("a media dos numeros pares é :", totalMedia)