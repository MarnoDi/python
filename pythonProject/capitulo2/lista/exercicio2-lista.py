numero = int(input("Digite um número de 5 dígitos: "))

numero1 = (numero // 10000) % 10
numero2 = (numero // 1000) % 10
numero3 = (numero // 100) % 10
numero4 = (numero // 10) % 10
numero5 = numero % 10

# // é a divisão inteira (ele ignora a parte decimal).
# % pega o ultimo numero (ex:12345, ele pega o 5)

print("  ", numero1)
print("  ", numero2)
print("  ", numero3)
print("  ", numero4)
print("  ", numero5)