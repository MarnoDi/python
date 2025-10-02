def calculoKmLitro(kmInicial, kmFinal, litrosConsumidos):
    calculoTotalKm = kmFinal - kmInicial / litrosConsumidos
    print(f"o calculo do consumo dos KM deu: {calculoTotalKm}")

def calculoDoLucro(precoDoCombustivel, valorRecebido, litrosConsumidos):
    calculoTotalDoLucro = valorRecebido - (litrosConsumidos * precoDoCombustivel)
    print(f"o calculo total do lucro foi de: {calculoTotalDoLucro}")


precoDoCombustivel = float(input("Digite o preço da gasolina: "))
kmInicial = float(input("Digite a quilometragem inicial: "))
kmFinal = float(input("Digite a quilometragem final: "))
litrosConsumidos = float(input("Digite quantos litros foram consumidos: "))
valorRecebido = float(input("Digite o valor recebido de cada passageiro: "))

calculoKmLitro(kmInicial, kmFinal, litrosConsumidos)
calculoDoLucro(precoDoCombustivel, valorRecebido, litrosConsumidos)