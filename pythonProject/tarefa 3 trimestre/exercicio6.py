def calculoMediaBimestral(notaFormativaUm, notaFormativaDois, notaProvaBimestral):
    calculoMediaFormativa = (notaFormativaUm + notaFormativaDois) / 2
    mediaBimestral = (calculoMediaFormativa * 0.3) + (notaProvaBimestral * 0.7)
    print(f"a media deu {mediaBimestral}")



notaFormativaUm = float(input("Digite a primeira nota formativa: "))
notaFormativaDois = float(input("Digite a segunda nota formativa: "))
notaProvaBimestral = float(input("Digite a nota da prova bimestral: "))
calculoMediaBimestral(notaFormativaUm, notaFormativaDois, notaProvaBimestral)