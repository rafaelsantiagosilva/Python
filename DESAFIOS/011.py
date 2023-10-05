titulo = "Exercício 11"
print("{:-^40}".format(titulo))
largura =  float(input("Digite a largura da parede que se deseja pintar [m]: "))
altura = float(input("Digite a altura da parede que se deseja pintar [m]: "))
area = altura * largura
print("\n{:-^30}".format("-"))
print("QUANTIDADE DE TINTA NECESSÁRIA:")
print("{:-^30}".format("-"))
print("{} Litros".format(area/2))
print("{:-^30}".format("-"))