def classificadorDeJogador(idade):
    if idade < 5:
        print("Idade baixa")
    elif 5 <= idade <= 7:
        print("Sua idade pode se classificar na categoria Infantil A")
    elif 8 <= idade <= 10:
        print("Sua idade pode se classificar na categoria Infantil B ")
    elif 11 <= idade <= 13:
        print("Sua idade pode se classificar na categria Juvenil A")
    elif 14 <= idade <= 17:
        print("Sua idade pode se classificar na categoria Juvenil B")
    else:
        print("Sua idade pode se classificar na categoria Senior")


idade = int(input("Digite sua idade: "))

classificadorDeJogador(idade)