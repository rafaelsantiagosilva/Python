print('{:-^35}'.format('Exercício 35'))
print("Digite os 3 comprimentos de retas: ")
l1 = float(input())
l2 = float(input())
l3 = float(input())

if (l1 + l2 > l3) and (l1 + l3 > l2) and (l2 + l3 > l1):
    print("Elas formam um triângulo!")
else:
    print("Elas não formam um triângulo!")