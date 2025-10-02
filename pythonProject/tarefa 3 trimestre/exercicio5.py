def calculoPesoIdeal(altura):
    calculoMedia = 62.1
    calculoBase =  44.7
    resultado = calculoMedia * altura - calculoBase
    print(f"O calculo do peso ideal é de: {resultado}")


altura = float(input("Digite sua altura: "))


calculoPesoIdeal(altura)