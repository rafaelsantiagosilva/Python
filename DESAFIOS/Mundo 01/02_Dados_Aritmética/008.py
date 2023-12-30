titulo = "Exercício 08"
print("{:-^40}".format(titulo))
metros =  float(input("Digite a medida [m]: "))
centimetros = metros*100
milimetros = centimetros*10
print("\n{:-^25}".format("-"))
print("CONVERSÃO: {}m".format(metros))
print("{:-^25}".format("-"))
print("{}cm \n{}mm".format(centimetros, milimetros))
print("{:-^25}".format("-"))