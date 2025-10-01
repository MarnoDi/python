def calculoValores(valor1, valor2, valor3, valor4):
    somaValores = valor1 + valor2 + valor3 + valor4
    resultado = somaValores - 10
    print(f"o calculo dos valores deu: {resultado}")



valor1 = int(input("Digite o primeiro numero: "))
valor2 = int(input("Digite o segundo numero: "))
valor3 = int(input("Digite o terceiro numero: "))
valor4 = int(input("Digite o quarto numero: "))

calculoValores(valor1, valor2, valor3, valor4)