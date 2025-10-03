def classificacaoDoProduto(numeroDoCodigo):
    if numeroDoCodigo == 1:
        print("Alimento não-perecível")
    elif 2 <= numeroDoCodigo <= 4:
        print("Alimento perecível")
    elif numeroDoCodigo == 5 or numeroDoCodigo == 6:
        print("Vestuário")
    elif numeroDoCodigo == 7:
        print("Higiene pessoal")
    elif 8 <= numeroDoCodigo <= 15:
        print("Limpeza e utensílios domésticos")
    else: print("Invalido")


numeroDoCodigo = int(input("Digite o codigo do produto: "))
classificacaoDoProduto(numeroDoCodigo)