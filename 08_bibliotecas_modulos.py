from math import sqrt, ceil, floor
print("{:-^30}".format('Aula 08'))
numero = int(input("Digite um número:" ))
raiz = sqrt(numero)
print("Raíz quadrada: {}".format(raiz))
print("Raiz arredondada para cima: {}".format(ceil(raiz)))
print("Raiz arredondada para baixo: {}".format(floor(raiz)))
print("\n{:=^25}".format('SORTEANDO NÚMERO'))
import random
aleatorio = random.random()
print("Número aletório qualquer: ", aleatorio)
aleatorio = random.randint(1, 10)
print("Número inteiro aleatório qualquer entre 1 e 10: ", aleatorio)