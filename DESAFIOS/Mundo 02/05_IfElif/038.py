print("{:-^35}".format('Exercício 38'))
n1 = float(input('Digite um número: '))
n2 = float(input('Digite mais um número: '))
if n1 > n2:
    print("{} é o maior!".format(n1))
elif n2 > n1:
    print('{} é o maior!'.format(n2))
else:
    print('{} e {} são iguais!'.format(n1, n2))