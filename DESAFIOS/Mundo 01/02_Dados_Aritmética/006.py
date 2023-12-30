import math
titulo = "Exercício 06"
print("{:-^40}".format(titulo))
numero =  int(input("Digite um número :"))
print("\n{:-^25}".format("-"))
print("INFORMAÇÕES SOBRE {}: ".format(numero))
print("{:-^25}".format("-"))
print("Dobro: {} \nTriplo: {} \nRaíz: {}".format(numero*2, numero*3, math.sqrt(numero)))