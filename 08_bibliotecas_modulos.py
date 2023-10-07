from math import sqrt, ceil, floor
print("{:-^30}".format('Aula 08'))
numero = int(input("Digite um número:" ))
raiz = sqrt(numero)
print("Raíz quadrada: {}".format(raiz))
print("Raiz arredondada para cima: {}".format(ceil(raiz)))
print("Raiz arredondada para baixo: {}".format(floor(raiz)))