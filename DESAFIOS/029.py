print("{:-^35}".format("Exercício 29"))
velocidade = float(input("Digite a velocidade do carro: "))
if velocidade > 80:
    print("\nMULTADO!")
    print("Valor da multa: R${}".format(7 * (velocidade-80)))
else:
    print("\nTudo em ordem!")