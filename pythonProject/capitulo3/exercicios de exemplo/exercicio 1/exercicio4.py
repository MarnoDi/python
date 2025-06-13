def calculaIMC(peso, altura):
    return peso / (altura ** 2)

#main
peso = float(input("digite seu peso: "))
altura = float(input("digite sua altura: "))

imc = calculaIMC(peso, altura)

print("o seu IMC é de : ", imc)