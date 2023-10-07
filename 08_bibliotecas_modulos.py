import math
print("{:-^30}".format('Aula 08'))
numero = int(input("Digite um número:" ))
raiz = math.sqrt(numero)
print("Raíz quadrada: {}".format(raiz))
print("Raiz arredondada para cima: {}".format(math.ceil(raiz)))
print("Raiz arredondada para baixo: {}".format(math.floor(raiz)))