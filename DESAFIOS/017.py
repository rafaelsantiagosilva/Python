from math import sqrt
print("{:-^30}".format('Exercício 17'))
cateto_op = float(input("Digite o valor do cateto oposto: "))
cateto_ad = float(input("Digite o valor do cateto adjascente: "))
hipotenusa = cateto_op**2 + cateto_ad**2
hipotenusa = sqrt(hipotenusa)
print("\nO valor da hipotenusa: {}".format(hipotenusa))