def operacoesdosNumeros(num1, num2):
    adicao = num1 + num2
    print(f"a adição deu: {adicao}")

    subtracao = num1 - num2
    print(f"a subtração deu: {subtracao}")

    divisao = num1 / num2
    print(f"a divisão deu: {divisao}")

    multipicacao = num1 * num2
    print(f"a multiplicação deu: {multipicacao}")

num1 = int(input("Digite o primeiro numero: "))
num2 = int(input("Digite o segundo numero: "))

operacoesdosNumeros(num1, num2)