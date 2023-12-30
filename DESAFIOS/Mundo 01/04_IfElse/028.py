from random import randint
print('{:-^35}'.format('Exercíco 28'))
print("\n{:=^30}".format('JOGO DA ADVINHAÇÃO'))
numero = randint(0, 5)
numero_user = int(input("Digite um número inteiro entre 0 e 5: "))
if numero_user == numero:
    print("PARABÉNS! Você acertou :D")
else:
    print("QUE PENA! Não foi dessa vez D:")