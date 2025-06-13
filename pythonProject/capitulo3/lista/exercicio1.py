def soma(numero, numero2):
    print("o resultado da soma é:", numero + numero2)

def subtracao(numero, numero2):
    print("o resultado da subtração é:", numero - numero2)

def multiplicacao(numero, numero2):
    print("o resultado da multiplicacao é:", numero * numero2)

def divisao(numero, numero2):
    resultado_divisao = numero / numero2
    print("o resultado da divisao é: ", resultado_divisao)


numero = int(input("digite o 1° numero:")) # input recebe entrada do usuario
numero2 = int(input("digite o 2° numero:")) # int converte aquilo em inteiros

soma(numero, numero2)
subtracao(numero, numero2)
multiplicacao(numero, numero2)
divisao(numero, numero2)