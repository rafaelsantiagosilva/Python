import math
print("{:-^30}".format('Exercício 18'))
ang = float(input("Digite o valor do ângulo: "))
ang = math.radians(ang)
print("{:=^30}\n{:^30}\n{:=^30}".format('', 'VALORES:', ''))
print("Seno: {}\nCosseno: {}\nTangente: {}\n{:=^30}".format(math.sin(ang), math.cos(ang), math.tan(ang), ''))