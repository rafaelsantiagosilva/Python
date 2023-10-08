print("{:-^40}".format('Exercício 42'))
print("Digite os 3 comprimentos de retas: ")
l1 = float(input())
l2 = float(input())
l3 = float(input())



if (l1 + l2 > l3) and (l1 + l3 > l2) and (l2 + l3 > l1):
    if l1 == l2 == l3:
        categoria = 'EQUILÁTERO'
    elif l1 == l2 or l1 == l3 or l2 == l3:
        categoria = 'ISÓCELES'
    else:
        categoria = 'ESCALENO'
    print("Elas formam um triângulo {}!".format(categoria))
else:
    print("Elas não formam um triângulo!")
    